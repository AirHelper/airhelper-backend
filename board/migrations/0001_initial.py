# Generated by Django 3.1.3 on 2021-08-21 07:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='제목')),
                ('content', models.CharField(max_length=1000, verbose_name='내용')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='작성일')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='회원id')),
            ],
            options={
                'verbose_name': '게시판',
                'db_table': 'board',
            },
        ),
        migrations.CreateModel(
            name='BoardMedia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_path', models.FileField(upload_to='board/% Y/% m/% d/', verbose_name='파일경로')),
                ('board', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='board.board', verbose_name='게시판id')),
            ],
            options={
                'verbose_name': '게시판 미디어 파일',
                'db_table': 'board_media',
            },
        ),
        migrations.CreateModel(
            name='BoardComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=100, verbose_name='덧글 내용')),
                ('board', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='board.board', verbose_name='게시판id')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='회원id')),
            ],
            options={
                'verbose_name': '게시판 덧글',
                'db_table': 'board_comment',
            },
        ),
    ]
