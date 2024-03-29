# Generated by Django 4.0.4 on 2022-09-18 17:41

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0005_alter_question_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='email',
            field=models.EmailField(max_length=150, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='question',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Ваше имя'),
        ),
        migrations.AlterField(
            model_name='question',
            name='phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, region=None, verbose_name='Телефон'),
        ),
    ]
