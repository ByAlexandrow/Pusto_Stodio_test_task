# Generated by Django 4.2.16 on 2024-10-08 14:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task_2', '0002_prize_player_prize_received'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='level',
            options={'verbose_name': 'Уровень', 'verbose_name_plural': 'Уровни'},
        ),
        migrations.AlterModelOptions(
            name='levelprize',
            options={'verbose_name': 'Награда за уровень', 'verbose_name_plural': 'Награда за уровень'},
        ),
        migrations.AlterModelOptions(
            name='player',
            options={'verbose_name': 'Игрок', 'verbose_name_plural': 'Игроки'},
        ),
        migrations.AlterModelOptions(
            name='playerlevel',
            options={'verbose_name': 'Уровень игрока', 'verbose_name_plural': 'Уровень игрока'},
        ),
        migrations.AlterModelOptions(
            name='prize',
            options={'verbose_name': 'Награда', 'verbose_name_plural': 'Награды'},
        ),
    ]
