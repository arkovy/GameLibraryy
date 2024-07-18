from django.views.generic import CreateView, DeleteView, ListView

from core.forms import GameCreate
from core.models import Game


class IndexView(ListView):
    template_name = 'game_list.html'
    model = Game
    context_object_name = 'games'

    def get_queryset(self):
        sort_by = self.request.GET.get('sort_by', 'name')
        sort_order = self.request.GET.get('sort_order', 'asc')
        if sort_order == 'desc':
            sort_by = '-' + sort_by
        return Game.objects.all().order_by(sort_by)


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


