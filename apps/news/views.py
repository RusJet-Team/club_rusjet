from django.shortcuts import render
from django.views.generic.detail import DetailView

from apps.news.models import News


class NewsDetailView(DetailView):

    model = News
    template_name = "news/news_detail.html"


def news_list(request):
    return render(request, "news/news_list.html")
