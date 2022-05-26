from django.db import migrations


def add_static_pages(apps, schema_editor):

    HalfStaticPage = apps.get_model("club", "HalfStaticPage")

    HalfStaticPage.objects.get_or_create(
        name="История клуба",
        slug="history",
        text="Здесь будет история клуба.",
    )
    HalfStaticPage.objects.get_or_create(
        name="Достижения",
        slug="achievements",
        text="Здесь будут наши достижения.",
    )
    HalfStaticPage.objects.get_or_create(
        name="Выступления",
        slug="performances",
        text="Здесь будет описание наших выступлений.",
    )



class Migration(migrations.Migration):

    dependencies = [
        ('club', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(
            add_static_pages,
        ),
    ]
