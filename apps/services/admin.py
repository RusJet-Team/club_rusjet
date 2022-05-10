from django.contrib import admin

from apps.main_page.mixins import AdminImagePreview
from apps.services.models import Service


@admin.register(Service)
class CarouselItemAdmin(AdminImagePreview, admin.ModelAdmin):
    list_display = (
        "name",
        "image_preview_list_page",
    )
    readonly_fields = ("image_preview_change_page",)

    class Media:
        css = {"all": ("assets/vendor/bootstrap/css/bootstrap.min.css",)}
