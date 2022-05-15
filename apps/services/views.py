from django.views.generic.detail import DetailView

from apps.services.models import ServiceItem


class ServiceDetailView(DetailView):

    model = ServiceItem
    template_name = "services/service-item.html"

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['now'] = timezone.now()
    #     return context
