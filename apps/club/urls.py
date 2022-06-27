from django.urls import path

from apps.club.views import ClubMembersView, HistoryAchievementsView

urlpatterns = [
    path("history/", HistoryAchievementsView.as_view(), name="history"),
    path("members/", ClubMembersView.as_view(), name="members"),
]
