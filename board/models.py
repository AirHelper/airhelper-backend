from django.db import models


# Create your models here.
class Board(models.Model):
    user = models.ForeignKey(
        'cert.CustomUser',
        on_delete=models.CASCADE,
        verbose_name='회원id'
    )
    title = models.CharField('제목', max_length=100, null=False)
    content = models.CharField('내용', max_length=1000, null=False)
    date_created = models.DateTimeField('작성일', auto_now_add=True)
    
    class Meta:
        db_table = 'board'
        verbose_name = '게시판'


class BoardMedia(models.Model):
    board = models.ForeignKey(
        'Board',
        on_delete=models.CASCADE,
        verbose_name='게시판id'
    )
    file_path = models.FileField('파일경로', upload_to='board/% Y/% m/% d/')
    
    class Meta:
        db_table = 'board_media'
        verbose_name = '게시판 미디어 파일'


class BoardComment(models.Model):
    board = models.ForeignKey(
        'Board',
        on_delete=models.CASCADE,
        verbose_name='게시판id'
    )
    user = models.ForeignKey(
        'cert.CustomUser',
        on_delete=models.CASCADE,
        verbose_name='회원id'
    )
    content = models.CharField('덧글 내용', max_length=100)
    
    class Meta:
        db_table = 'board_comment'
        verbose_name = '게시판 덧글'