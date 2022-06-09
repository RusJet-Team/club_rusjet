from django.urls import path

from apps.main_page.views import HomePageView, PartnerDetailView

urlpatterns = [
    path("", HomePageView.as_view(), name="index"),
    path("partners/<slug:slug>/", PartnerDetailView.as_view(), name="partners"),
]
