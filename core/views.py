from django.shortcuts import render, redirect
from django.views.generic import CreateView, DeleteView, ListView

from core.forms import GameCreate
from core.models import Post


class IndexView(ListView):
    template_name = 'game_list.html'
    model = Post
    context_object_name = 'posts'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.select_related('author').all()

        return context


class GameCreateView(CreateView):
    template_name = 'game_create.html'
    form_class = GameCreate
    success_url = '/game-create/'

    def form_valid(self, form):
        form.save(user=self.request.user)
        return redirect(self.success_url)

    def get_initial(self):
        return {
            'title': 'Введите назване игры',
        }


class PostDeleteView(DeleteView):
    template_name = 'game_delete.html'
    model = Post
    success_url = '/'
