import datetime
import urllib

import factory
from django.contrib.auth import get_user_model
from django.core.files.base import ContentFile
from django.db.models import signals
from factory.fuzzy import FuzzyDate
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

    name = factory.Faker("text", max_nb_chars=70, locale="ru_RU")
    title = factory.Faker("text", max_nb_chars=150, locale="ru_RU")
    text = factory.Faker("text", max_nb_chars=1000, locale="ru_RU")
    pub_date = FuzzyDate(
        datetime.date(2022, 3, 1),
        datetime.date(2022, 10, 31),
    )
    pub_user = factory.Iterator(User.objects.all(), cycle=True)

    @factory.post_generation
    def image(self, created, extracted, **kwargs):
        if not created:
            return

        image = urllib.request.urlopen("https://picsum.photos/1200/900").read()
        self.image.save(self.name + ".jpg", ContentFile(image), save=False)

    @factory.post_generation
    def category(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            category = extracted
            add_category = NewsCategory.objects.filter(name=category)
            self.category.add(*add_category)
            return

        at_least = 1
        num = kwargs.get("num", None)
        how_many = num or at_least

        category_count = NewsCategory.objects.count()
        how_many = min(category_count, how_many)

        category = NewsCategory.objects.order_by("?")[:how_many]
        self.category.add(*category)

    @factory.post_generation
    def event_bool(self, created, extracted, **kwargs):
        if not created:
            return
        if extracted:
            event_bool = extracted
            self.event_bool = event_bool

    @factory.post_generation
    def video_url(self, created, extracted, **kwargs):
        if not created:
            return
        if extracted:
            url = "https://www.youtube.com/watch?v=yC4jG-wuVoc"
            self.video_url = url

    @factory.post_generation
    def event_date(self, created, extracted, **kwargs):
        if not created:
            return
        if self.event_bool is True:
            date = fake.date_between(start_date="today", end_date="+1y")
            self.event_date = date

    @factory.post_generation
    def geolocation_url(self, created, extracted, **kwargs):
        if not created:
            return
        if self.event_bool is True:
            url = """<div style="position:relative;overflow:hidden;"><a href="https://yandex.ru/maps/213/moscow/?utm_medium=mapframe&utm_source=maps" style="color:#eee;font-size:12px;position:absolute;top:0px;">Москва</a><a href="https://yandex.ru/maps/213/moscow/?ll=37.622504%2C55.753215&utm_medium=mapframe&utm_source=maps&z=10" style="color:#eee;font-size:12px;position:absolute;top:14px;">Яндекс Карты — транспорт, навигация, поиск мест</a><iframe src="https://yandex.ru/map-widget/v1/-/CGW1A~q" width="560" height="400" frameborder="1" allowfullscreen="true" style="position:relative;"></iframe></div>"""  # Noqa
            self.geolocation_url = url
