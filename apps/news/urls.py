from django.urls import path

from apps.news.views import news_detail, news_list

urlpatterns = [
    path("news/", news_list, name="news"),
    path("new/", news_detail, name="new"),
]
