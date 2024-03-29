from django.db.models import Q
from django.shortcuts import render
from django.utils.timezone import now
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView

from apps.main_page.models import CarouselItem, Partner
from apps.news.models import News
from apps.services.models import ServiceItem


class HomePageView(TemplateView):

    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["carousel_items"] = CarouselItem.objects.all()
        context["services"] = ServiceItem.objects.all()

        context["news"] = News.objects.filter(
            Q(event_bool=True) & Q(event_date__gte=now().date()) | Q(event_bool=False)
        ).order_by("-pub_date")[:4]

        return context


class PartnerDetailView(DetailView):

    model = Partner
    template_name = "main-page/partners-detail.html"


def bad_request(request, exception):
    return render(request, "misc/400.html", {"path": request.path}, status=400)


def permission_denied(request, exception):
    return render(request, "misc/403.html", {"path": request.path}, status=403)


def page_not_found(request, exception):
    return render(request, "misc/404.html", {"path": request.path}, status=404)


def server_error(request):
    return render(request, "misc/500.html", status=500)
