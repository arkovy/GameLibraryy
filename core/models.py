from django.contrib.auth.models import User
from django.db import models


class TimeAbstractModel(models.Model):

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


def image_upload_to(instance, filename):
    return f'images/{filename}'


class Game(TimeAbstractModel):
    DIFFICULTY_EASY = 1
    DIFFICULTY_MEDIUM = 2
    DIFFICULTY_HARD = 3
    DIFFICULTY = (
        (DIFFICULTY_EASY, 'Easy'),
        (DIFFICULTY_MEDIUM, 'Medium'),
        (DIFFICULTY_HARD, 'Hard')
    )

    name = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    developer = models.CharField(max_length=100)
    icon = models.ImageField(upload_to=image_upload_to, blank=True, null=True)
    difficulty = models.PositiveSmallIntegerField(choices=DIFFICULTY)

    def __str__(self):
        return self.name
