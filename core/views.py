from django.urls import reverse
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from core.forms import GameCreate
from core.models import Game


class IndexView(ListView):
    template_name = 'game_list.html'
    model = Game
    context_object_name = 'games'


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

