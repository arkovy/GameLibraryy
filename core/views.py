from django.shortcuts import redirect
from django.views.generic import CreateView, DeleteView, ListView

from core.forms import GameCreate
from core.models import Game


class IndexView(ListView):
    template_name = 'game_list.html'
    model = Game
    context_object_name = 'games'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['games'] = Game.objects.all()

        return context


class GameCreateView(CreateView):
    template_name = 'game_create.html'
    form_class = GameCreate
    success_url = '/'

    def form_valid(self, form):
        form.save(user=self.request.user)
        return redirect(self.success_url)

    def get_initial(self):
        return {
            'title': 'Введите назване игры',
        }


class GameDeleteView(DeleteView):
    template_name = 'game_delete.html'
    model = Game
    success_url = '/'
