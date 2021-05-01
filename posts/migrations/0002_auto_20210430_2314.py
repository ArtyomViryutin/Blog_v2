# Generated by Django 3.2 on 2021-04-30 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации комментария'),
        ),
        migrations.AlterField(
            model_name='post',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации поста'),
        ),
        migrations.AlterField(
            model_name='viewing',
            name='view_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата просмотра поста'),
        ),
    ]
