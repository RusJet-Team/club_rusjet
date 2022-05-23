from django.urls import path

from apps.news.views import CategoryNewsListView, NewsDetailView, NewsListView, SearchNewsResultsView

urlpatterns = [
    path("news/", NewsListView.as_view(), name="news_list"),
    path("news/<int:pk>/", NewsDetailView.as_view(), name="news_detail"),
    path("news/category/<slug:slug>/", CategoryNewsListView.as_view(), name="news_category"),
    path("news/search-results/", SearchNewsResultsView.as_view(), name="search_results"),
]
