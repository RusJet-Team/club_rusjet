# from django.shortcuts import get_object_or_404
from django.views.generic.base import TemplateView


class EquipmentView(TemplateView):

    template_name = "equipment/equipment.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context["achievements"] = get_object_or_404(HalfStaticPage, slug="achievements")
        return context


class EquipmentDetailView(TemplateView):

    template_name = "equipment/equipment-detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context["achievements"] = get_object_or_404(HalfStaticPage, slug="achievements")
        return context
