from django.db import models


class Room(models.Model):
    title = models.CharField('제목', max_length=20, null=False, unique=True)
    password = models.CharField('비밀번호', max_length=6, null=False, default='none')
    verbose_left = models.IntegerField('레드팀 수', null=False, default=0)
    verbose_right = models.IntegerField('블루팀 수', null=False, default=0)
    time = models.IntegerField('게임 시간', null=False, default=0)
    game_type = models.ForeignKey(
        'room.GameType',
        on_delete=models.CASCADE,
        verbose_name='게임종류',
        default=1
    )

    class Meta:
        db_table = 'room'
        verbose_name = '방'


class GameType(models.Model):
    type_name = models.CharField('게임 타입명', max_length=10, null=False)
    
    class Meta:
        db_table = 'gametype'
        verbose_name = '게임타입'