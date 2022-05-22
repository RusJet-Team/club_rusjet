# from django.shortcuts import render
from django.views.generic.base import TemplateView

from apps.main_page.models import CarouselItem, Partner
from apps.news.models import News
from apps.services.models import ServiceItem


class HomePageView(TemplateView):

    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["carousel_items"] = CarouselItem.objects.all()
        context["partners"] = Partner.objects.all()
        context["services"] = ServiceItem.objects.all()
        context["news"] = News.objects.all().order_by("pub_date")[:4]

        return context


class PortfolioDetailsView(TemplateView):

    template_name = "partners.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["partners"] = Partner.objects.all()
        return context


# def index(request):
#     # post_list = Post.objects.all()
#     # paginator = Paginator(post_list, 10)
#     # page_number = request.GET.get("page")
#     # page = paginator.get_page(page_number)
#     return render(request, "index.html")
