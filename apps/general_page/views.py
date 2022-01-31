from django.shortcuts import render
from django.utils import timezone

from apps.general_page.models import MainImage, SocialNetwork


def general_main(request):
    images = MainImage.objects.all()
    networks = SocialNetwork.objects.all()
    context = {
        "images": images,
        "networks": networks,
        "year": timezone.now().year,
    }
    return render(request, "main.html", context)


def plug(request):
    return render(request, "page_in_dev.html")
