# Generated by Django 3.1.3 on 2021-08-30 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='alive',
            field=models.BooleanField(default=True, verbose_name='생존 여부'),
        ),
    ]
