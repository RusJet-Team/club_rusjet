from django.contrib import admin
from django.contrib.auth.models import Group

from apps.main_page.mixins import AdminImagePreview
from apps.main_page.models import CarouselItem, Partner
from config.utils.app_list import get_app_list

admin.AdminSite.get_app_list = get_app_list


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
    search_fields = ("name",)
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "name",
                    "short_description",
                    "text",
                    "url",
                    "image",
                    "image_preview_change_page",
                ),
            },
        ),
    )


admin.site.site_header = "Администрирование сайта клуба "
admin.site.unregister(Group)
