from django import forms

from core.models import Game


class GameCreate(forms.ModelForm):

    class Meta:
        model = Game
        fields = ('name', 'genre', 'developer', 'difficulty', 'icon')
