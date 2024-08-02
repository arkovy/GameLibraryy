from django.shortcuts import render
from django.views.generic import CreateView, DeleteView, ListView

from core.forms import GameCreate
from core.models import Game


class IndexView(ListView):
    template_name = 'game_list.html'
    model = Game
    context_object_name = 'games'

    def get_queryset(self):
        search_name = self.request.GET.get('search_name', '')
        search_genre = self.request.GET.get('search_genre', '')
        search_difficulty = self.request.GET.get('search_difficulty', '')
        sort_by = self.request.GET.get('sort_by', 'name')
        sort_order = self.request.GET.get('sort_order', 'asc')

        games = Game.objects.all()

        if search_name:
            games = games.filter(name__icontains=search_name)

        if search_genre:
            games = games.filter(genre__icontains=search_genre)

        if search_difficulty:
            difficulty_mapping = {
                'easy': Game.DIFFICULTY_EASY,
                'medium': Game.DIFFICULTY_MEDIUM,
                'hard': Game.DIFFICULTY_HARD,
            }
            difficulty_value = difficulty_mapping.get(search_difficulty)
            if difficulty_value is not None:
                games = games.filter(difficulty=difficulty_value)

        if sort_order == 'desc':
            sort_by = f'-{sort_by}'

        return games.order_by(sort_by)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_name'] = self.request.GET.get('search_name', '')
        context['search_genre'] = self.request.GET.get('search_genre', '')
        context['search_difficulty'] = self.request.GET.get('search_difficulty', '')
        context['sort_by'] = self.request.GET.get('sort_by', 'name')
        context['sort_order'] = self.request.GET.get('sort_order', 'asc')
        return context


class GameCreateView(CreateView):
    template_name = 'game_create.html'
    form_class = GameCreate
    success_url = '/'


class GameDeleteView(DeleteView):
    template_name = 'game_delete.html'
    model = Game
    success_url = '/'


class GameView(DeleteView):
    template_name = 'game_info.html'
    model = Game
    context_object_name = 'game'


