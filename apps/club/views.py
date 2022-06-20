from django.shortcuts import get_object_or_404
from django.views.generic.base import TemplateView

from apps.club.models import ClubMember, HalfStaticPage


class ClubMembersView(TemplateView):

    template_name = "club/members.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["members"] = ClubMember.objects.all()
        return context


class HistoryView(TemplateView):

    template_name = "club/history.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["history"] = get_object_or_404(HalfStaticPage, slug="history")
        return context


class AchievementsView(TemplateView):

    template_name = "club/achievements.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["achievements"] = get_object_or_404(HalfStaticPage, slug="achievements")
        return context
