from django.shortcuts import render

from apps.general_page.models import MainImage


def general_main(request):
    images = MainImage.objects.all()
    count = range(MainImage.objects.count())
    print(count)
    context = {
        "images": images,
        "range": count,
    }
    return render(request, "main.html", context)
