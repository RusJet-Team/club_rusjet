# Generated by Django 4.0.4 on 2022-05-17 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0005_carouselitem_button_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='partner',
            name='url',
            field=models.URLField(blank=True, verbose_name='Ссылка на сайт'),
        ),
    ]
