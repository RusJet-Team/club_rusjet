from django.contrib import admin
from django.utils.html import format_html

from apps.main_page.mixins import AdminImagePreview, HideOnNavPanelAdminModelMixin
from apps.services.models import ServiceCarouselImage, ServiceItem


class ServiceCarouselImagesInline(AdminImagePreview, admin.TabularInline):
    model = ServiceCarouselImage
    readonly_fields = ("image_preview",)
    verbose_name = "Изображение"
    verbose_name_plural = "Изображения"
    extra = 1
    classes = ("collapsible",)
    model.__str__ = lambda self: ""


@admin.register(ServiceItem)
class ServiceItemAdmin(AdminImagePreview, admin.ModelAdmin):
    inlines = (ServiceCarouselImagesInline,)
    list_display = (
        "name",
        "image_preview_list_page",
    )
    fields = (
        "name",
        "short_description",
        "image",
        "image_change_page",
        "text",
        "slug",
    )
    readonly_fields = ("image_change_page",)

    @admin.display(description="Значок услуги на главной")
    def image_change_page(self, obj):
        return format_html('<img src="{}" height="300" style="object-fit: contain;" />'.format(obj.image.url))


@admin.register(ServiceCarouselImage)
class CarouselItemAdmin(HideOnNavPanelAdminModelMixin, admin.ModelAdmin):
    pass
