import factory
from django.core.management.base import BaseCommand

from apps.equipment.factories import (
    EquipmentBrendFactory,
    EquipmentCategoryFactory,
    EquipmentItemFactory,
    EquipmentItemImageFactory,
    EquipmentItemYoutubeVideoUrlFactory,
    EquipmentSubCategoryFactory,
)
from apps.equipment.models import (
    EquipmentBrend,
    EquipmentCategory,
    EquipmentItem,
    EquipmentItemImage,
    EquipmentItemYoutubeVideoUrl,
    EquipmentSubCategory,
)

EQUIPMENT_CATEGORIES = [
    "Двигатели",
    "Электроника",
    "Комплектующие",
]

EQUIPMENT_SUBCATEGORIES_ENGINE = [
    "Турбореактивные",
    "Бензиновые",
    "Электрические",
]

EQUIPMENT_SUBCATEGORIES_ELECTRONICS = [
    "Аппаратура",
    "Рулевые машинки",
    "Аккумуляторы",
]

EQUIPMENT_SUBCATEGORIES_PARTS = [
    "Для реактивных двигателей",
    "Тяги, наконечники, петли",
    "Качалки",
]

EQUIPMENT_ENGINE_BREND = [
    "JetCat",
    "KingTech",
    "TurboJet",
]

EQUIPMENT_ELECTRONICS_BREND = [
    "PowerBox",
    "Futaba",
]

EQUIPMENT_PARTS_BREND = [
    "ElectronRetracts",
    "JetTronics",
]


class MyException(Exception):
    pass


class Command(BaseCommand):
    help = "Fill Data Base with test data equipment"

    def handle(self, *args, **options):
        try:
            with factory.Faker.override_default_locale("ru_RU"):
                if EquipmentCategory.objects.count() == 0:

                    for category_name in EQUIPMENT_CATEGORIES:
                        EquipmentCategoryFactory(name=category_name)

                if EquipmentSubCategory.objects.count() == 0:

                    engine = EquipmentCategory.objects.get(name="Двигатели")
                    electronics = EquipmentCategory.objects.get(name="Электроника")
                    parts = EquipmentCategory.objects.get(name="Комплектующие")

                    for subcategory_name in EQUIPMENT_SUBCATEGORIES_ENGINE:
                        EquipmentSubCategoryFactory(name=subcategory_name, category=engine)
                    for subcategory_name in EQUIPMENT_SUBCATEGORIES_ELECTRONICS:
                        EquipmentSubCategoryFactory(name=subcategory_name, category=electronics)
                    for subcategory_name in EQUIPMENT_SUBCATEGORIES_PARTS:
                        EquipmentSubCategoryFactory(name=subcategory_name, category=parts)

                if EquipmentBrend.objects.count() == 0:

                    subcategory_engine = EquipmentSubCategory.objects.get(name="Турбореактивные")
                    subcategory_electronics = EquipmentSubCategory.objects.get(name="Аппаратура")
                    subcategory_parts = EquipmentSubCategory.objects.get(name="Для реактивных двигателей")

                    for brend_name in EQUIPMENT_ENGINE_BREND:
                        EquipmentBrendFactory(name=brend_name, subcategory=subcategory_engine)
                    for brend_name in EQUIPMENT_ELECTRONICS_BREND:
                        EquipmentBrendFactory(name=brend_name, subcategory=subcategory_electronics)
                    for brend_name in EQUIPMENT_PARTS_BREND:
                        EquipmentBrendFactory(name=brend_name, subcategory=subcategory_parts)

                if EquipmentItem.objects.count() == 0:

                    subcategory_engine = EquipmentSubCategory.objects.get(name="Турбореактивные")
                    subcategory_electronics = EquipmentSubCategory.objects.get(name="Аппаратура")
                    brend_engine_1 = EquipmentBrend.objects.get(name="JetCat")
                    brend_engine_2 = EquipmentBrend.objects.get(name="KingTech")
                    brend_engine_3 = EquipmentBrend.objects.get(name="TurboJet")
                    brend_electronics = EquipmentBrend.objects.get(name="PowerBox")

                    EquipmentItemFactory.create_batch(10, subcategory=subcategory_engine, brend=brend_engine_1)
                    EquipmentItemFactory.create_batch(10, subcategory=subcategory_engine, brend=brend_engine_2)
                    EquipmentItemFactory.create_batch(10, subcategory=subcategory_engine, brend=brend_engine_3)
                    EquipmentItemFactory.create_batch(30, subcategory=subcategory_electronics, brend=brend_electronics)

                if EquipmentItemImage.objects.count() == 0:
                    EquipmentItemImageFactory.create_batch(120)

                if EquipmentItemYoutubeVideoUrl.objects.count() == 0:
                    EquipmentItemYoutubeVideoUrlFactory.create_batch(80)

            self.stdout.write(self.style.SUCCESS("The database is filled with test data"))
        except MyException:
            self.stdout.write(self.style.ERROR("The database is already filled with standard test data."))
