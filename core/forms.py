from django import forms

from core.models import Game


class GameCreate(forms.ModelForm):

    class Meta:
        model = Game
        fields = ('name', 'genre', 'developer', 'difficulty', 'icon')

    def save(self, user=None, commit=True):
        game = super(GameCreate, self).save(commit=False)
        game.save()

        self.save_m2m()
        return game
