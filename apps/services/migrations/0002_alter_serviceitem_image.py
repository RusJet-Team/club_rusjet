# Generated by Django 4.0.4 on 2022-08-28 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='serviceitem',
            name='image',
            field=models.ImageField(help_text='Изображения только в формате png 100*100', upload_to='images/services/', verbose_name='Значок на главной странице'),
        ),
    ]
