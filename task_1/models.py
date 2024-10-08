from django.db import models
from django.utils import timezone


class Player(models.Model):
    username = models.CharField(
        unique=True,
        max_length=20,
    )
    forst_login_record = models.DateTimeField(
        null=True,
        blank=True,
    )
    all_points = models.IntegerField(
        default=0,
    )


    def __str__(self):
        return self.username


    def record_login(self):
        if not self.first_login_record:
            self.first_login_record = timezone.now()
            self.save()


    def add_points(self, points):
        self.all_points += points
        self.save()


    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
    

class Boost(models.Model):
    player = models.ForeignKey(
        Player,
        related_name='boosts',
        on_delete=models.CASCADE,
    )
    boost_type = models.CharField(
        max_length=100,
    )
    award_quantity = models.IntegerField(
        default=0,
    )
    awarded_time = models.DateTimeField(
        auto_now_add=True,
    )


    def __str__(self):
        return f'+{self.award_quantity}'
    

    class Meta:
        verbose_name = 'Бонус'
        verbose_name_plural = 'Бонусы'


    @classmethod
    def award_boost(cls, player, boost_type, award_quantity):
        boost, created = cls.objects.get_or_create(player=player, boost_type=boost_type)
        boost.award_quantity += award_quantity
        boost.save()
