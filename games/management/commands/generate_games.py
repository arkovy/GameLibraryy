from django.core.management.base import BaseCommand
from games.models import Game  # замените `myapp` на имя вашего приложения
import random


class Command(BaseCommand):
    help = 'Generate a specified number of games'

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='Number of games to generate')

    def handle(self, *args, **kwargs):
        count = kwargs['count']
        difficulties = [Game.DIFFICULTY_EASY, Game.DIFFICULTY_MEDIUM, Game.DIFFICULTY_HARD]
        for _ in range(count):
            name = f'Game {random.randint(1, 10000)}'
            genre = 'Genre'
            developer = 'Developer'
            difficulty = random.choice(difficulties)  # Выбираем случайное значение для difficulty
            Game.objects.create(name=name, genre=genre, developer=developer, difficulty=difficulty)
            self.stdout.write(self.style.SUCCESS(f'Successfully generated game: {name} with difficulty: {difficulty}'))
