# Generated by Django 4.0.4 on 2022-05-22 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_alter_news_pub_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='pub_date',
            field=models.DateField(auto_now_add=True, verbose_name='Дата публикации'),
        ),
    ]