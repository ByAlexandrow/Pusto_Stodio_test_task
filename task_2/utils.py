import csv
from django.db.models import Prefetch
from django.utils import timezone

from task_2.models import PlayerLevel, LevelPrize, Prize


def assign_prize_to_player(player_id, level_id):
    try:
        player_level = PlayerLevel.objects.get(player__player_id=player_id, level__id=level_id)
        if player_level.is_completed:
            level_prizes = LevelPrize.objects.filter(level__id=level_id)
            for level_prize in level_prizes:
                Prize.objects.create(
                    player=player_level.player,
                    title=level_prize.prize.title,
                    received=timezone.now()
                )
            return f"Призы за уровень {level_id} успешно присвоены игроку {player_id}."
        else:
            return f"Уровень {level_id} не пройден игроком {player_id}."
    except PlayerLevel.DoesNotExist:
        return f"Запись о прохождении уровня {level_id} игроком {player_id} не найдена."


def export_player_level_data_to_csv(file_path):
    player_levels = PlayerLevel.objects.select_related('player', 'level').prefetch_related(
        Prefetch('level__levelprize_set', queryset=LevelPrize.objects.select_related('prize'))
    )

    with open(file_path, 'w', newline='') as csvfile:
        fieldnames = ['player_id', 'level_title', 'is_completed', 'prize_title']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        
        for player_level in player_levels:
            player_id = player_level.player.player_id
            level_title = player_level.level.title
            is_completed = player_level.is_completed
            prizes = player_level.level.levelprize_set.all()
            
            if prizes:
                for prize in prizes:
                    writer.writerow({
                        'player_id': player_id,
                        'level_title': level_title,
                        'is_completed': is_completed,
                        'prize_title': prize.prize.title
                    })
            else:
                writer.writerow({
                    'player_id': player_id,
                    'level_title': level_title,
                    'is_completed': is_completed,
                    'prize_title': ''
                })

    return f"Данные успешно экспортированы в {file_path}"
