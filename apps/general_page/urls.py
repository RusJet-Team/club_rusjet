from django.urls import path

from apps.general_page.views import general_main, plug

urlpatterns = [
    path(
        "",
        general_main,
        name="main",
    ),
    path(
        "plug/",
        plug,
        name="plug",
    ),
]
