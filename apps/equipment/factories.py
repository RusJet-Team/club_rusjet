import urllib.request

import factory
from django.core.files.base import ContentFile
from faker import Faker

from apps.equipment.models import (
    EquipmentBrend,
    EquipmentCategory,
    EquipmentItem,
    EquipmentItemImage,
    EquipmentItemYoutubeVideoUrl,
    EquipmentSubCategory,
)

fake = Faker(["ru-RU"])


class EquipmentCategoryFactory(factory.django.DjangoModelFactory):
    """Create EquipmentCategory objects."""

    class Meta:
        model = EquipmentCategory

    name = factory.Sequence(lambda n: fake.unique.word())

    @factory.post_generation
    def image(self, created, extracted, **kwargs):
        if not created:
            return

        image = urllib.request.urlopen("https://picsum.photos/400/400").read()
        self.image.save(str(self.id) + ".jpg", ContentFile(image), save=False)


class EquipmentSubCategoryFactory(factory.django.DjangoModelFactory):
    """Create EquipmentSubCategory objects."""

    class Meta:
        model = EquipmentSubCategory

    name = factory.Sequence(lambda n: fake.unique.word())
    category = factory.Iterator(EquipmentCategory.objects.all(), cycle=True)

    @factory.post_generation
    def image(self, created, extracted, **kwargs):
        if not created:
            return

        image = urllib.request.urlopen("https://picsum.photos/400/400").read()
        self.image.save(str(self.id) + ".jpg", ContentFile(image), save=False)


class EquipmentBrendFactory(factory.django.DjangoModelFactory):
    """Create EquipmentBrend objects."""

    class Meta:
        model = EquipmentBrend

    name = factory.Sequence(lambda n: fake.unique.word())
    subcategory = factory.Iterator(EquipmentSubCategory.objects.all(), cycle=True)

    @factory.post_generation
    def image(self, created, extracted, **kwargs):
        if not created:
            return

        image = urllib.request.urlopen("https://picsum.photos/400/400").read()
        self.image.save(str(self.id) + ".jpg", ContentFile(image), save=False)


class EquipmentItemFactory(factory.django.DjangoModelFactory):
    """Create EquipmentItem objects."""

    class Meta:
        model = EquipmentItem

    name = factory.Faker("word", locale="ru_RU")
    title = factory.Faker("text", max_nb_chars=250, locale="ru_RU")
    tech_data = factory.Faker("text", max_nb_chars=1000, locale="ru_RU")
    subcategory = factory.Iterator(EquipmentSubCategory.objects.all(), cycle=True)
    brend = factory.Iterator(EquipmentBrend.objects.all(), cycle=True)


class EquipmentItemImageFactory(factory.django.DjangoModelFactory):
    """Create EquipmentItemImage objects."""

    class Meta:
        model = EquipmentItemImage

    equipment = factory.Iterator(EquipmentItem.objects.all(), cycle=True)

    @factory.post_generation
    def image(self, created, extracted, **kwargs):
        if not created:
            return

        image = urllib.request.urlopen("https://picsum.photos/900/900").read()
        self.image.save(str(self.id) + ".jpg", ContentFile(image), save=False)


class EquipmentItemYoutubeVideoUrlFactory(factory.django.DjangoModelFactory):
    """Create EquipmentItemYoutubeVideoUrl objects."""

    class Meta:
        model = EquipmentItemYoutubeVideoUrl

    video_url = "https://www.youtube.com/embed/-V48J_PdBpM"
    equipment = factory.Iterator(EquipmentItem.objects.all(), cycle=True)


# class EquipmentItemDocumentFactory(factory.django.DjangoModelFactory):
#     """Create EquipmentItemDocument objects."""

#     class Meta:
#         model = EquipmentItemDocument

#     equipment = factory.Iterator(EquipmentItem.objects.all(), cycle=True)

#     @factory.post_generation
#     def document(self, created, extracted, **kwargs):
#         if not created:
#             return

#         pdf = FPDF()
#         pdf.add_page()
#         pdf.set_font('helvetica', size=12)
#         pdf.cell(txt="hello world")
#         self.document = pdf.output("hello_world.pdf")
