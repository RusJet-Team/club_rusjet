import urllib.request

import factory
from django.core.files.base import ContentFile
from faker import Faker

from apps.projects.models import Project, ProjectCategory, ProjectImage

fake = Faker(["ru-RU"])


class ProjectCategoryFactory(factory.django.DjangoModelFactory):
    """Create ProjectCategory objects."""

    class Meta:
        model = ProjectCategory

    name = factory.Sequence(lambda n: fake.unique.word())


class ProjectFactory(factory.django.DjangoModelFactory):
    """Create Project objects."""

    class Meta:
        model = Project

    name = factory.Faker("word", locale="ru_RU")
    title = factory.Faker("text", max_nb_chars=250, locale="ru_RU")
    text = factory.Faker("text", max_nb_chars=1000, locale="ru_RU")
    category = factory.Iterator(ProjectCategory.objects.all(), cycle=True)


class ProjectImageFactory(factory.django.DjangoModelFactory):
    """Create ProjectImage objects."""

    class Meta:
        model = ProjectImage

    project = factory.Iterator(Project.objects.all(), cycle=True)

    @factory.post_generation
    def image(self, created, extracted, **kwargs):
        if not created:
            return

        image = urllib.request.urlopen("https://picsum.photos/1200/900").read()
        self.image.save(str(self.id) + ".jpg", ContentFile(image), save=False)
