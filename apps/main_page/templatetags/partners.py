from django import template

from apps.main_page.models import Partner

register = template.Library()


@register.simple_tag()
def get_partners():
    partners = Partner.objects.all()
    return partners
