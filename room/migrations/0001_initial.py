# Generated by Django 3.1.3 on 2021-08-02 08:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GameType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_name', models.CharField(max_length=10, verbose_name='게임 타입명')),
            ],
            options={
                'verbose_name': '게임타입',
                'db_table': 'gametype',
            },
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20, unique=True, verbose_name='제목')),
                ('password', models.CharField(default='none', max_length=6, verbose_name='비밀번호')),
                ('verbose_left', models.IntegerField(default=0, verbose_name='레드팀 수')),
                ('verbose_right', models.IntegerField(default=0, verbose_name='블루팀 수')),
                ('time', models.IntegerField(default=0, verbose_name='게임 시간')),
                ('game_type', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='room.gametype', verbose_name='게임종류')),
            ],
            options={
                'verbose_name': '방',
                'db_table': 'room',
            },
        ),
    ]
