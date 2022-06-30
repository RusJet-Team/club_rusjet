from django import template

from apps.equipment.models import LastViewedEquipmentItem

register = template.Library()


@register.simple_tag()
def get_last_viewed(session):
    items = LastViewedEquipmentItem.objects.filter(session=session)
    return items
