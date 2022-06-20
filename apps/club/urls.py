from django.urls import path

from apps.club.views import AchievementsView, ClubMembersView, HistoryView

urlpatterns = [
    path("history/", HistoryView.as_view(), name="history"),
    path("members/", ClubMembersView.as_view(), name="members"),
    path("achievements/", AchievementsView.as_view(), name="achievements"),
]
