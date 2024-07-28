from django.urls import reverse
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

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

        queryset = Game.objects.all()

        if search_name:
            queryset = queryset.filter(name__icontains=search_name)
        if search_genre:
            queryset = queryset.filter(genre__icontains=search_genre)
        if search_difficulty:
            queryset = queryset.filter(difficulty__icontains=search_difficulty)

        if sort_order == 'desc':
            sort_by = '-' + sort_by

        return queryset.order_by(sort_by)


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


class GameEditView(UpdateView):
    template_name = 'game_edit.html'
    model = Game
    fields = ('name', 'genre', 'developer', 'difficulty', 'icon')

    def get_success_url(self):
        return reverse('game-info', kwargs={'pk': self.object.pk})


