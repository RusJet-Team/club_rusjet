from django.db import migrations


def change_static_pages(apps, schema_editor):

    HalfStaticPage = apps.get_model("club", "HalfStaticPage")

    HalfStaticPage.objects.filter(slug="history").update(
        name="История и достижения клуба",
        text="Здесь будет история и достижения клуба.",
    )

    HalfStaticPage.objects.filter(slug="achievements").delete()



class Migration(migrations.Migration):

    dependencies = [
        ('club', '0004_remove_clubmember_email_clubmember_achievements'),
    ]

    operations = [
        migrations.RunPython(
            change_static_pages,
        ),
    ]
