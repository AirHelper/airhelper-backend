from django.db import models


# Create your models here.
class Game(models.Model):
    title = models.CharField('제목', max_length=20, null=False, unique=True)
    password = models.CharField('비밀번호', max_length=6, null=False, default='none')
    verbose_left = models.IntegerField('레드팀 수', null=False, default=0)
    verbose_right = models.IntegerField('블루팀 수', null=False, default=0)
    time = models.IntegerField('게임 시간', null=False, default=0)
    game_type = models.ForeignKey(
        'room.GameType',
        on_delete=models.CASCADE,
        verbose_name='게임종류',
        default=0
    )

    class Meta:
        db_table = 'game'
        verbose_name = '게임'


class Player(models.Model):
    game = models.ForeignKey(
        'game.Game',
        on_delete=models.CASCADE,
        verbose_name='게임ID'
    )
    user = models.ForeignKey(
        'cert.CustomUser',
        on_delete=models.CASCADE,
        verbose_name='회원id'
    )
    team = models.CharField('팀', max_length=20, null=False, default='레드팀')
    is_admin = models.BooleanField('방장 여부', null=False, default=False)

    class Meta:
        db_table = 'player'
        verbose_name = '플레이어'
