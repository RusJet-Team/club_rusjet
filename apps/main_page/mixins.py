from django.contrib import admin
from django.utils.html import format_html


class AdminImagePreview:
    """
    Mixin makes preview for uploaded images.
    Need to add parameters in admin class
    list_display = ("image_preview_list_page",)
    readonly_fields = ("image_preview_change_page",)
    """

    @admin.display(description="Превью")
    def image_preview_change_page(self, obj):
        return format_html('<img src="{}" height="300" style="object-fit: contain;" />'.format(obj.image.url))

    @admin.display(description="Превью")
    def image_preview_list_page(self, obj):
        if obj.image:
            return format_html('<img src="{}" height="50" style="object-fit: contain;" />'.format(obj.image.url))

    @admin.display(description="Превью изображения")
    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" height="50" style="object-fit: contain;" />'.format(obj.image.url))


class HideOnNavPanelAdminModelMixin:
    """Mixin hides model from admin main page(nav. panel)."""

    def has_module_permission(self, request):
        return False
