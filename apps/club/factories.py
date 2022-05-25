import urllib

import factory
from django.core.files.base import ContentFile
from faker import Faker

from apps.club.models import ClubMember

fake = Faker(["ru-RU"])


class ClubMemberFactory(factory.django.DjangoModelFactory):
    """Create ClubMember objects."""

    class Meta:
        model = ClubMember

    first_name = factory.Faker("first_name", locale="ru_RU")
    last_name = factory.Faker("last_name", locale="ru_RU")
    middle_name = factory.Faker("middle_name", locale="ru_RU")
    vocation = factory.Faker("job", locale="ru_RU")
    email = factory.Faker("email", locale="ru_RU")

    @factory.post_generation
    def image(self, created, extracted, **kwargs):
        if not created:
            return

        image = urllib.request.urlopen("https://picsum.photos/900/1200").read()
        self.image.save(self.first_name + self.last_name + ".jpg", ContentFile(image), save=False)
