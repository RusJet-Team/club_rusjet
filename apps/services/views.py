from django.views.generic.detail import DetailView

from apps.services.models import ServiceCarouselImage, ServiceItem, ServiceYoutubeVideoUrl


class ServiceDetailView(DetailView):

    model = ServiceItem
    template_name = "services/service-item.html"

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)
        context["carousel_images"] = ServiceCarouselImage.objects.filter(service=self.object)
        context["youtube_urls"] = ServiceYoutubeVideoUrl.objects.filter(service=self.object)
        return self.render_to_response(context)
