from django.db.models import Q
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from apps.news.models import News


class NewsDetailView(DetailView):

    model = News
    template_name = "news/news_detail.html"


class NewsListView(ListView):

    model = News
    template_name = "news/news_list.html"
    paginate_by = 10


class CategoryNewsListView(ListView):

    model = News
    template_name = "news/category_news_list.html"
    paginate_by = 10

    def get_queryset(self, *args, **kwargs):
        return News.objects.filter(category__slug=self.kwargs["slug"])


class SearchNewsResultsView(ListView):
    model = News
    template_name = "news/search_results.html"

    def get_queryset(self):
        query = self.request.GET.get("search")
        object_list = News.objects.filter(
            Q(name__icontains=query) | Q(title__icontains=query) | Q(text__icontains=query)
        )
        return object_list
