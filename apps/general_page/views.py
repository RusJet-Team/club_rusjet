from django.shortcuts import render


def general_main(request):
    return render(request, "main.html")
