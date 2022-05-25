import urllib

import factory
from django.core.files.base import ContentFile
from faker import Faker

from apps.main_page.models import CarouselItem, Partner

fake = Faker(["ru-RU"])


class PartnerFactory(factory.django.DjangoModelFactory):
    """Create Partner objects."""

    class Meta:
        model = Partner

    name = factory.Faker("company", locale="ru_RU")
    url = factory.Faker("url", locale="ru_RU")

    @factory.post_generation
    def image(self, created, extracted, **kwargs):
        if not created:
            return

        image = urllib.request.urlopen("https://picsum.photos/200/150").read()
        self.image.save(self.name + ".jpg", ContentFile(image), save=False)


class CarouselItemFactory(factory.django.DjangoModelFactory):
    """Create CarouselItem objects."""

    class Meta:
        model = CarouselItem

    name = factory.Faker("word", locale="ru_RU")
    title = factory.Faker("text", max_nb_chars=100, locale="ru_RU")
    text = factory.Faker("text", max_nb_chars=200, locale="ru_RU")
    button_text = factory.Faker("word", locale="ru_RU")
    button_url = factory.Faker("url", locale="ru_RU")

    @factory.post_generation
    def image(self, created, extracted, **kwargs):
        if not created:
            return

        image = urllib.request.urlopen("https://picsum.photos/1200/900").read()
        self.image.save(self.name + ".jpg", ContentFile(image), save=False)
