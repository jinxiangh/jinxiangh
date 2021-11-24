# Generated by Django 3.1.7 on 2021-04-06 10:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news_app', '0010_auto_20210402_2053'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='ticket',
            new_name='token',
        ),
        migrations.AlterField(
            model_name='answer',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 6, 18, 6, 2, 784838), verbose_name='评论时间'),
        ),
        migrations.AlterField(
            model_name='hotnews',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 6, 18, 6, 2, 783840), verbose_name='发布时间'),
        ),
        migrations.AlterField(
            model_name='question',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 6, 18, 6, 2, 783840), verbose_name='提问时间'),
        ),
    ]
