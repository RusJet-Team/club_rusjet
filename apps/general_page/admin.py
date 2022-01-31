from django.contrib import admin
from django.utils.html import format_html

from apps.general_page.mixins import AdminImagePreview
from apps.general_page.models import MainImage, SocialNetwork


@admin.register(MainImage)
class MainImageAdmin(AdminImagePreview, admin.ModelAdmin):
    list_display = (
        "name",
        "image_preview_list_page",
    )
    readonly_fields = ("image_preview_change_page",)

    def has_add_permission(self, request, obj=None):
        """Remove the save and add new button."""
        return False

    def has_delete_permission(self, request, obj=None):
        """Remove the delete button."""
        return False

    class Media:
        css = {"all": ("main/css/mdb.min.css",)}


@admin.register(SocialNetwork)
class SocialNetworkAdmin(admin.ModelAdmin):
    list_display = (
        "type",
        "is_visible",
        "get_social_url",
    )

    @admin.display(description="Ссылка")
    def get_social_url(self, obj):
        return format_html("<a href='{url}'>{url}</a>", url=obj.url)


# @admin.register(InscriptionOnManePage)
# class InscriptionOnManePageAdmin(admin.ModelAdmin):
#     list_display = (
#         "name",
#         "value",
#     )
