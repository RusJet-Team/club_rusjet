from django import template

from apps.equipment.models import EquipmentBrend, EquipmentCategory, EquipmentSubCategory

register = template.Library()


@register.simple_tag()
def get_categories():
    categories = EquipmentCategory.objects.all().order_by("name")
    return categories


@register.simple_tag()
def get_subcategories(category):
    subcategories = EquipmentSubCategory.objects.filter(category=category).order_by("name")
    return subcategories


@register.simple_tag()
def get_brends(subcategory):
    brends = EquipmentBrend.objects.filter(subcategory=subcategory).order_by("name")
    return brends
