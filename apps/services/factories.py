import urllib

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

    @factory.post_generation
    def carousel_images(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            carousel_images = extracted
            self.carousel_images.add(*carousel_images)
            return

        at_least = 1
        num = kwargs.get("num", None)
        how_many = num or at_least

        carousel_images_count = ServiceCarouselImage.objects.count()
        how_many = min(carousel_images_count, how_many)

        carousel_images = ServiceCarouselImage.objects.order_by("?")[:how_many]
        self.carousel_images.add(*carousel_images)


class ServiceCarouselImageFactory(factory.django.DjangoModelFactory):
    """Create ServiceCarouselImage objects."""

    class Meta:
        model = ServiceCarouselImage

    @factory.post_generation
    def image(self, created, extracted, **kwargs):
        if not created:
            return

        image = urllib.request.urlopen("https://picsum.photos/600/400").read()
        self.image.save(str(self.id) + ".jpg", ContentFile(image), save=False)
