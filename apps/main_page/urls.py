# from django.conf import settings
# from django.conf.urls.static import static
# from django.contrib import admin
from django.urls import path

from apps.main_page.views import HomePageView, PortfolioDetailsView

urlpatterns = [
    path("", HomePageView.as_view(), name="index"),
    path("portfolio/", PortfolioDetailsView.as_view(), name="portfolio"),
]
