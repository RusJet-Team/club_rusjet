from django.contrib import admin

from apps.main_page.mixins import AdminImagePreview
from apps.main_page.models import CarouselItem, Partner


@admin.register(CarouselItem)
class CarouselItemAdmin(AdminImagePreview, admin.ModelAdmin):
    list_display = (
        "name",
        "image_preview_list_page",
    )
    readonly_fields = ("image_preview_change_page",)


@admin.register(Partner)
class PartnerAdmin(AdminImagePreview, admin.ModelAdmin):
    list_display = (
        "name",
        "image_preview_list_page",
    )
    readonly_fields = ("image_preview_change_page",)
