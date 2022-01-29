from django.core.files import File
from django.db import migrations


def add_images(apps, schema_editor):

    MainImage = apps.get_model("general_page", "MainImage")

    myfile_1 = File(open("./fixtures/main_page/first.jpg", "rb"))
    myfile_2 = File(open("./fixtures/main_page/second.jpg", "rb"))
    myfile_3 = File(open("./fixtures/main_page/third.jpg", "rb"))

    MainImage.objects.create(
        name="Первый слайд",
        image=myfile_1,
    )
    MainImage.objects.create(
        name="Второй слайд",
        image=myfile_2,
    )
    MainImage.objects.create(
        name="Третий слайд",
        image=myfile_3,
    )


class Migration(migrations.Migration):

    dependencies = [
        ("general_page", "0001_initial"),
    ]

    operations = [migrations.RunPython(add_images)]
