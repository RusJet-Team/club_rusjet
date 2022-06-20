from django.contrib import admin

from apps.equipment.models import (
    EquipmentBrend,
    EquipmentCategory,
    EquipmentItem,
    EquipmentItemDocument,
    EquipmentItemImage,
    EquipmentItemYoutubeVideoUrl,
    EquipmentSubCategory,
)
from apps.main_page.mixins import AdminImagePreview, HideOnNavPanelAdminModelMixin


class EquipmentItemImageInline(AdminImagePreview, admin.TabularInline):
    model = EquipmentItemImage
    readonly_fields = ("image_preview",)
    verbose_name = "Изображение оборудования"
    verbose_name_plural = "Изображения оборудования"
    extra = 1
    classes = ("collapsible",)
    model.__str__ = lambda self: ""


class EquipmentItemDocumentInline(AdminImagePreview, admin.TabularInline):
    model = EquipmentItemDocument
    verbose_name = "Документ"
    verbose_name_plural = "Документы"
    extra = 1
    classes = ("collapsible",)
    model.__str__ = lambda self: ""


class EquipmentItemYoutubeVideoUrlInline(AdminImagePreview, admin.TabularInline):
    model = EquipmentItemYoutubeVideoUrl
    verbose_name = "Youtube ссылка"
    verbose_name_plural = "Youtube ссылки"
    extra = 1
    classes = ("collapsible",)
    model.__str__ = lambda self: ""


@admin.register(EquipmentCategory)
class EquipmentCategoryAdmin(AdminImagePreview, admin.ModelAdmin):
    list_display = (
        "name",
        "image_preview_list_page",
    )


@admin.register(EquipmentSubCategory)
class EquipmentSubCategoryAdmin(AdminImagePreview, admin.ModelAdmin):
    list_display = (
        "name",
        "image_preview_list_page",
    )
    list_filter = ("category__name",)


@admin.register(EquipmentBrend)
class EquipmentBrendAdmin(AdminImagePreview, admin.ModelAdmin):
    list_display = (
        "name",
        "image_preview_list_page",
    )
    list_filter = (
        "subcategory__category__name",
        "subcategory__name",
    )


@admin.register(EquipmentItemDocument)
class EquipmentItemDocumentAdmin(HideOnNavPanelAdminModelMixin, admin.ModelAdmin):
    list_display = ("id",)


@admin.register(EquipmentItemImage)
class EquipmentItemImageAdmin(HideOnNavPanelAdminModelMixin, admin.ModelAdmin):
    pass


@admin.register(EquipmentItemYoutubeVideoUrl)
class EquipmentItemYoutubeVideoUrlAdmin(HideOnNavPanelAdminModelMixin, admin.ModelAdmin):
    pass


@admin.register(EquipmentItem)
class EquipmentItemAdmin(AdminImagePreview, admin.ModelAdmin):
    inlines = (
        EquipmentItemImageInline,
        EquipmentItemDocumentInline,
        EquipmentItemYoutubeVideoUrlInline,
    )
    list_display = (
        "name",
        "brend",
        "subcategory",
    )
    list_filter = (
        "subcategory__category__name",
        "subcategory__name",
    )
    search_fields = (
        "name",
        "brend__name",
        "subcategory__name",
    )
