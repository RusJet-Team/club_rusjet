# Generated by Django 4.0.4 on 2022-08-28 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('club', '0007_alter_clubmember_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='halfstaticpageyoutubevideourl',
            options={'ordering': ['my_order'], 'verbose_name': 'Ссылка на видео YouTube', 'verbose_name_plural': 'Ссылки на видео YouTube'},
        ),
        migrations.AddField(
            model_name='halfstaticpageyoutubevideourl',
            name='my_order',
            field=models.PositiveIntegerField(default=0, verbose_name='Порядок отображения'),
        ),
    ]