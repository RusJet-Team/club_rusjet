# Generated by Django 4.0.4 on 2022-05-08 21:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0002_partner_alter_carouselitem_options_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='partner',
            old_name='logo',
            new_name='image',
        ),
    ]