# Generated by Django 4.0.4 on 2022-05-23 19:14

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_alter_news_pub_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='text',
            field=ckeditor.fields.RichTextField(verbose_name='Основной текст'),
        ),
    ]
