from django import template

from apps.news.models import News, NewsCategory

register = template.Library()


@register.simple_tag()
def get_categories():
    categories = NewsCategory.objects.all()
    return categories


@register.simple_tag()
def get_upcoming_events():
    news = News.objects.filter(category__name="Мероприятия").order_by("event_date")[:5]
    return news
