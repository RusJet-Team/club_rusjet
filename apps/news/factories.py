import factory
from django.contrib.auth import get_user_model
from django.db.models import signals
from faker import Faker

from apps.news.models import News, NewsCategory

User = get_user_model()
fake = Faker(["ru-RU"])


@factory.django.mute_signals(signals.post_save)
class UserFactory(factory.django.DjangoModelFactory):
    """Creates User object."""

    class Meta:
        model = User
        django_get_or_create = ["username"]

    username = factory.Sequence(lambda n: "user_%d" % (User.objects.count()))
    password = "rusjet"
    first_name = factory.Faker("first_name")
    last_name = factory.Faker("last_name")
    email = factory.LazyAttribute(lambda obj: f"{obj.username}@rusjet.com")

    @classmethod
    def _create(cls, model_class, *args, **kwargs):
        """Override the default ``_create`` with our custom call.
        The method has been taken from factory_boy manual. Without it
        password for users is being created without HASH and doesn't work
        right.
        """

        manager = cls._get_manager(model_class)
        return manager.create_user(*args, **kwargs)


class NewsCategoryFactory(factory.django.DjangoModelFactory):
    """Create NewsCategory objects."""

    class Meta:
        model = NewsCategory

    name = factory.Sequence(lambda n: fake.unique.word())


class NewsFactory(factory.django.DjangoModelFactory):
    """Create News objects."""

    class Meta:
        model = News

    name = factory.Sequence(lambda n: fake.unique.word())
    # title =
    # text =
    # pub_date =
    # image =
    # pub_user =
    # category =
    # video_url =
    # geolocation_url =
    # event_bool =
    # event_date =
