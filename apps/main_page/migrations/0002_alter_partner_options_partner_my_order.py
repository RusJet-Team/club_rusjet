# Generated by Django 4.0.4 on 2022-08-28 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='partner',
            options={'ordering': ['my_order'], 'verbose_name': 'Партнёр', 'verbose_name_plural': 'Партнёры'},
        ),
        migrations.AddField(
            model_name='partner',
            name='my_order',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
