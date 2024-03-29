# Generated by Django 4.0.4 on 2022-09-18 17:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0003_alter_servicecarouselimage_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ServiceYoutubeVideoUrl',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video_url', models.CharField(max_length=150, verbose_name='Ссылка на видео YouTube')),
                ('my_order', models.PositiveIntegerField(default=0, verbose_name='Порядок отображения')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='services.serviceitem', verbose_name='Услуга')),
            ],
            options={
                'verbose_name': 'Ссылка на видео YouTube',
                'verbose_name_plural': 'Ссылки на видео YouTube',
                'ordering': ['my_order'],
            },
        ),
    ]
