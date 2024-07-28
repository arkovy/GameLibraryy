from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(
        max_length=150,
        required=True,
        help_text='Обязательное поле. Не более 150 символов. Только буквы, цифры и символы.',
        widget=forms.TextInput(attrs={'placeholder': 'Имя пользователя'})
    )
    email = forms.EmailField(required=True, help_text='Введите действительный адрес электронной почты.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
