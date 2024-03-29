# Generated by Django 4.0.4 on 2022-08-28 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equipment', '0009_equipmentrequest'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='equipmentitem',
            options={'ordering': ['my_order'], 'verbose_name': 'Оборудование', 'verbose_name_plural': 'Оборудование'},
        ),
        migrations.AlterModelOptions(
            name='equipmentitemdocument',
            options={'ordering': ['my_order'], 'verbose_name': 'Документ единицы оборудования', 'verbose_name_plural': 'Документы единицы оборудования'},
        ),
        migrations.AlterModelOptions(
            name='equipmentitemimage',
            options={'ordering': ['my_order'], 'verbose_name': 'Изображение единицы оборудования', 'verbose_name_plural': 'Изображения единицы оборудования'},
        ),
        migrations.AlterModelOptions(
            name='equipmentitemyoutubevideourl',
            options={'ordering': ['my_order'], 'verbose_name': 'Ссылка на видео YouTube', 'verbose_name_plural': 'Ссылки на видео YouTube'},
        ),
        migrations.AddField(
            model_name='equipmentitem',
            name='my_order',
            field=models.PositiveIntegerField(default=0, verbose_name='Порядок отображения'),
        ),
        migrations.AddField(
            model_name='equipmentitemdocument',
            name='my_order',
            field=models.PositiveIntegerField(default=0, verbose_name='Порядок отображения'),
        ),
        migrations.AddField(
            model_name='equipmentitemimage',
            name='my_order',
            field=models.PositiveIntegerField(default=0, verbose_name='Порядок отображения'),
        ),
        migrations.AddField(
            model_name='equipmentitemyoutubevideourl',
            name='my_order',
            field=models.PositiveIntegerField(default=0, verbose_name='Порядок отображения'),
        ),
    ]
