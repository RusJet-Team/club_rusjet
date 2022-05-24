from django import template

from apps.projects.models import ProjectCategory

register = template.Library()


@register.simple_tag()
def get_project_categories():
    categories = ProjectCategory.objects.all()
    return categories
