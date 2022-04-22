# from django.conf import settings
# from django.conf.urls.static import static
# from django.contrib import admin
from django.urls import path

from apps.main_page.views import HomePageView

urlpatterns = [
    path("", HomePageView.as_view(), name="index"),
]
