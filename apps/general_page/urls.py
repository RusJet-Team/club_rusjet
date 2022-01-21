from django.urls import path

from apps.general_page.views import general_main

urlpatterns = [
    path("", general_main),
]
