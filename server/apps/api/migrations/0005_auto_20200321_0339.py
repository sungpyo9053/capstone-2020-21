# Generated by Django 3.0.4 on 2020-03-20 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20200320_1455'),
    ]

    operations = [
        migrations.AddField(
            model_name='clothessetreview',
            name='comment',
            field=models.CharField(default='한줄평을 입력해주세요.', max_length=100),
        ),
        migrations.AddField(
            model_name='user',
            name='nickname',
            field=models.CharField(default='닉네임을 입력해주세요.', max_length=30),
        ),
        migrations.AlterField(
            model_name='clothessetreview',
            name='review',
            field=models.IntegerField(choices=[(1, 'cold'), (2, 'little_cold'), (3, 'nice'), (4, 'little_hot'), (5, 'hot')]),
        ),
    ]
