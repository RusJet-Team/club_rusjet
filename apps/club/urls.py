from django.urls import path

from apps.club.views import ClubMembersView, achievements, history, performances

urlpatterns = [
    path("history/", history, name="history"),
    path("achievements/", achievements, name="achievements"),
    path("members/", ClubMembersView.as_view(), name="members"),
    path("performances", performances, name="performances"),
]
