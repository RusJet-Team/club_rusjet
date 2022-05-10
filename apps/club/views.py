from django.shortcuts import render
from django.views.generic.base import TemplateView

from apps.club.models import ClubMember


class ClubMembersView(TemplateView):

    template_name = "club/members.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["members"] = ClubMember.objects.all()
        return context


def history(request):
    return render(request, "club/history.html")


def achievements(request):
    return render(request, "club/achievements.html")


def performances(request):
    return render(request, "club/performances.html")
