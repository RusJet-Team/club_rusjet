import random

import factory
from django.core.management.base import BaseCommand

from apps.club.factories import ClubMemberFactory
from apps.main_page.factories import CarouselItemFactory, PartnerFactory
from apps.news.factories import NewsCategoryFactory
from apps.news.models import NewsCategory
from apps.services.factories import ServiceCarouselImageFactory, ServiceItemFactory

CATEGORIES = [
    "Мероприятия",
    "О клубе",
    "Оборудование",
    "Новые самолеты",
    "Жизнь команды",
]


class MyException(Exception):
    pass


class Command(BaseCommand):
    help = "Fill Data Base with test data"

    def handle(self, *args, **options):
        try:
            if NewsCategory.objects.count() > 0:
                raise MyException()
            with factory.Faker.override_default_locale("ru_RU"):
                for category_name in CATEGORIES:
                    NewsCategoryFactory(name=category_name)

                ClubMemberFactory.create_batch(10)

                PartnerFactory.create_batch(6)

                CarouselItemFactory.create_batch(7)

                ServiceCarouselImageFactory.create_batch(30)

                for _ in range(7):
                    nums = random.randint(1, 5)
                    ServiceItemFactory(carousel_images__num=nums)

            self.stdout.write(self.style.SUCCESS("The database is filled with test data"))
        except MyException:
            self.stdout.write(
                self.style.ERROR(
                    "The database is already filled with standard test "
                    "data. To top up individual tables, use the arguments."
                )
            )
