# Generated by Django 4.0.4 on 2022-05-17 23:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='name',
            field=models.CharField(max_length=200, verbose_name='Название новости'),
        ),
        migrations.AlterField(
            model_name='news',
            name='title',
            field=models.CharField(max_length=500, verbose_name='Краткое описание'),
        ),
        migrations.AlterField(
            model_name='newscategory',
            name='slug',
            field=models.SlugField(blank=True, help_text='Если оставить пустым, заполнится транслитом название категории', max_length=70, verbose_name='URL категории'),
        ),
    ]
