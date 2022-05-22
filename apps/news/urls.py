from django.urls import path

from apps.news.views import NewsDetailView, news_list

urlpatterns = [
    path("news/", news_list, name="news"),
    path("news/<int:pk>/", NewsDetailView.as_view(), name="news_detail"),
]
