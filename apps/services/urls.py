from django.urls import path

from apps.services.views import ServiceDetailView

urlpatterns = [
    path("services/<slug:slug>/", ServiceDetailView.as_view(), name="serviceitem-detail"),
]
