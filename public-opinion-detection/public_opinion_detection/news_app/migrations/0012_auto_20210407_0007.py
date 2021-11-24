# Generated by Django 3.1.7 on 2021-04-06 16:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news_app', '0011_auto_20210406_1806'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='iconUrl',
            new_name='avatarurl',
        ),
        migrations.AlterField(
            model_name='answer',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 7, 0, 7, 49, 143148), verbose_name='评论时间'),
        ),
        migrations.AlterField(
            model_name='hotnews',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 7, 0, 7, 49, 143148), verbose_name='发布时间'),
        ),
        migrations.AlterField(
            model_name='question',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 7, 0, 7, 49, 143148), verbose_name='提问时间'),
        ),
    ]
