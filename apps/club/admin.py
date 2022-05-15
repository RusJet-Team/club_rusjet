from django.contrib import admin

from apps.club.models import ClubMember
from apps.main_page.mixins import AdminImagePreview


@admin.register(ClubMember)
class CarouselItemAdmin(AdminImagePreview, admin.ModelAdmin):
    list_display = (
        "vocation",
        "image_preview_list_page",
    )
    readonly_fields = ("image_preview_change_page",)
