import urllib.request

import factory
from django.core.files.base import ContentFile

from apps.services.models import ServiceCarouselImage, ServiceItem


class ServiceItemFactory(factory.django.DjangoModelFactory):
    """Create ServiceItem objects."""

    class Meta:
        model = ServiceItem

    name = factory.Faker("word", locale="ru_RU")
    short_description = factory.Faker("text", max_nb_chars=250, locale="ru_RU")
    text = factory.Faker("text", max_nb_chars=1000, locale="ru_RU")

    @factory.post_generation
    def image(self, created, extracted, **kwargs):
        if not created:
            return

        image = urllib.request.urlopen("https://picsum.photos/70/70").read()
        self.image.save(self.name + ".jpg", ContentFile(image), save=False)


class ServiceCarouselImageFactory(factory.django.DjangoModelFactory):
    """Create ServiceCarouselImage objects."""

    class Meta:
        model = ServiceCarouselImage

    service = factory.Iterator(ServiceItem.objects.all(), cycle=True)

    @factory.post_generation
    def image(self, created, extracted, **kwargs):
        if not created:
            return

        image = urllib.request.urlopen("https://picsum.photos/600/400").read()
        self.image.save(str(self.id) + ".jpg", ContentFile(image), save=False)
