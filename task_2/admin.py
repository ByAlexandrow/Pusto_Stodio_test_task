from django.contrib import admin

from task_2.models import Player, Level, Prize, PlayerLevel, LevelPrize


admin.site.register(Player)
admin.site.register(Level)
admin.site.register(Prize)
admin.site.register(PlayerLevel)
admin.site.register(LevelPrize)
