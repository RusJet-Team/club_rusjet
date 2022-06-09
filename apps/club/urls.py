from django.urls import path

from apps.club.views import ClubMembersView, HistoryView, PerformancesView

urlpatterns = [
    path("history/", HistoryView.as_view(), name="history"),
    path("members/", ClubMembersView.as_view(), name="members"),
    path("performances", PerformancesView.as_view(), name="performances"),
]
