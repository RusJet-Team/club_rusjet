from django import template

from apps.services.models import ServiceItem

register = template.Library()


@register.simple_tag()
def get_service_names():
    names = ServiceItem.objects.values("name", "slug")
    return names
