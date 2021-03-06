# Generated by Django 4.0.4 on 2022-06-21 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('club', '0002_add_static_pages'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clubmember',
            name='email',
            field=models.EmailField(blank=True, help_text='Если указать, будет доступен для связи на сайте', max_length=150, unique=True, verbose_name='Электронная почта'),
        ),
    ]
