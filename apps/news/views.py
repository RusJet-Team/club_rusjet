from django.shortcuts import render


def news_list(request):
    return render(request, "news/news_list.html")


def news_detail(request):
    return render(request, "news/news_detail.html")
