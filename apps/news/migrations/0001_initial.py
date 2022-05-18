# Generated by Django 4.0.4 on 2022-05-17 23:17

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
            name='NewsCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название категории')),
                ('slug', models.SlugField(help_text='Если оставить пустым, заполнится транслитом название категории', max_length=70, verbose_name='URL категории')),
            ],
            options={
                'verbose_name': 'Название категории',
                'verbose_name_plural': 'Названия категорий',
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Дата мероприятия')),
                ('title', models.CharField(max_length=500, verbose_name='Дата мероприятия')),
                ('text', models.TextField(verbose_name='Основной текст')),
                ('pub_date', models.DateField(auto_now_add=True, verbose_name='Дата публикации')),
                ('image', models.ImageField(blank=True, upload_to='images/news', verbose_name='Фотография для новости')),
                ('video_url', models.URLField(blank=True, help_text='Если необходимо вставить видео, укажите ссылку на Youtube или Rutube', verbose_name='Ссылка на видео')),
                ('geolocation_url', models.TextField(blank=True, help_text='Если нужна геолокация,необходимо вставить кусок html кода с https://yandex.ru/maps', verbose_name='Геолокация')),
                ('event_bool', models.BooleanField(default=False, verbose_name='Мероприятие')),
                ('event_date', models.DateField(blank=True, null=True, verbose_name='Дата мероприятия')),
                ('category', models.ManyToManyField(related_name='news', to='news.newscategory', verbose_name='Категории')),
                ('pub_user', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.RESTRICT, to=settings.AUTH_USER_MODEL, verbose_name='Автор новости')),
            ],
            options={
                'verbose_name': 'Новость',
                'verbose_name_plural': 'Новости',
                'ordering': ['pub_date'],
            },
        ),
        migrations.AddConstraint(
            model_name='news',
            constraint=models.UniqueConstraint(fields=('name', 'pub_date', 'title'), name='unique_name_for_pub_date'),
        ),
    ]