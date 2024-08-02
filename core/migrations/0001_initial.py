# Generated by Django 5.0.6 on 2024-06-30 10:26

import core.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100)),
                ('genre', models.CharField(max_length=100)),
                ('developer', models.CharField(max_length=100)),
                ('icon', models.ImageField(blank=True, null=True, upload_to=core.models.image_upload_to)),
                ('difficulty', models.PositiveSmallIntegerField(choices=[(1, 'Easy'), (2, 'Medium'), (3, 'Hard')])),
            ],
            options={
                'abstract': False,
            },
        ),
    ]