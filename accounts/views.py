from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate


# Представление для регистрации
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Вход после регистрации
            return redirect('home')  # Перенаправление на домашнюю страницу или другую страницу
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})


# Представление для входа
def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')  # Перенаправление на домашнюю страницу или другую страницу
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})

