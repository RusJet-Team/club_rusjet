from django.views.generic.detail import DetailView

from apps.services.models import ServiceItem


class ServiceDetailView(DetailView):

    model = ServiceItem
    template_name = "services/service-item.html"
