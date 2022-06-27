from django.views.generic.base import TemplateView

from apps.club.models import ClubMember, HalfStaticPage


class ClubMembersView(TemplateView):

    template_name = "club/members.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["members"] = ClubMember.objects.all()
        return context


class HistoryAchievementsView(TemplateView):

    template_name = "club/history_achievements.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["history"] = HalfStaticPage.objects.get(slug="history")
        return context
