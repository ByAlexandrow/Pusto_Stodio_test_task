from django.db import models


class Player(models.Model):
    player_id = models.CharField(
        max_length=100,
    )

    class Meta:
        verbose_name = 'Игрок'
        verbose_name_plural = 'Игроки'
    
    
class Level(models.Model):
    title = models.CharField(
        max_length=100,
    )
    order = models.IntegerField(
        default=0,
    )

    class Meta:
        verbose_name = 'Уровень'
        verbose_name_plural = 'Уровни'

    
class Prize(models.Model):
    player = models.ForeignKey(
        Player,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    title = models.CharField(
        max_length=50,
    )
    received = models.DateTimeField(
        null=True,
        blank=True
    )

    class Meta:
        verbose_name = 'Награда'
        verbose_name_plural = 'Награды'
    
    
class PlayerLevel(models.Model):
    player = models.ForeignKey(
        Player,
        on_delete=models.CASCADE,
    )
    level = models.ForeignKey(
        Level,
        on_delete=models.CASCADE,
    )
    completed = models.DateField()
    is_completed = models.BooleanField(
        default=False,
    )
    score = models.PositiveIntegerField(
        default=0,
    )

    class Meta:
        verbose_name = 'Уровень игрока'
        verbose_name_plural = 'Уровень игрока'
    
    
class LevelPrize(models.Model):
    level = models.ForeignKey(
        Level,
        on_delete=models.CASCADE
    )
    prize = models.ForeignKey(
        Prize,
        on_delete=models.CASCADE
    )
    received = models.DateField()

    class Meta:
        verbose_name = 'Награда за уровень'
        verbose_name_plural = 'Награда за уровень'
