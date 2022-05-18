# Generated by Django 4.0.4 on 2022-05-05 22:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CarouselItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Название слайда')),
                ('order_id', models.SmallIntegerField(verbose_name='Порядковый номер слайда')),
                ('title', models.CharField(max_length=150, verbose_name='Заголовок слайда')),
                ('text', models.TextField(verbose_name='Текст слайда')),
                ('button_text', models.CharField(max_length=20, verbose_name='Текст кнопки')),
                ('image', models.ImageField(upload_to='images/main_page', verbose_name='Картинка слайда')),
            ],
            options={
                'verbose_name': 'Слайд на главной странице.',
                'verbose_name_plural': 'Слайды на главной странице.',
            },
        ),
    ]