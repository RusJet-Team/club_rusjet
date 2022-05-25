from django.urls import path

from apps.club.views import AchievementsView, ClubMembersView, HistoryView, PerformancesView

urlpatterns = [
    path("history/", HistoryView.as_view(), name="history"),
    path("achievements/", AchievementsView.as_view(), name="achievements"),
    path("members/", ClubMembersView.as_view(), name="members"),
    path("performances", PerformancesView.as_view(), name="performances"),
]
