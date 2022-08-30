from django import template
from django.utils.timezone import now

from apps.news.models import News, NewsCategory

register = template.Library()


@register.simple_tag()
def get_categories():
    categories = NewsCategory.objects.all()
    return categories


@register.inclusion_tag("news/includes/upcoming_events.html")
def get_upcoming_events():
    time_now = now().date()
    news = News.objects.filter(category__name="Мероприятия", event_date__gte=time_now).order_by("event_date")[:5]
    return {"upcoming_events": news}
