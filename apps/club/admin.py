from django.contrib import admin

from apps.club.models import ClubMember, HalfStaticPage, HalfStaticPageImage, HalfStaticPageYoutubeVideoUrl
from apps.main_page.mixins import AdminImagePreview, HideOnNavPanelAdminModelMixin


@admin.register(ClubMember)
class ClubMemberAdmin(AdminImagePreview, admin.ModelAdmin):
    list_display = (
        "vocation",
        "image_preview_list_page",
    )
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "first_name",
                    "last_name",
                    "middle_name",
                    "vocation",
                    "achievements",
                    "image",
                    "image_preview_change_page",
                ),
            },
        ),
    )
    readonly_fields = ("image_preview_change_page",)


class HalfStaticPageImageInline(AdminImagePreview, admin.TabularInline):
    model = HalfStaticPageImage
    readonly_fields = ("image_preview",)
    verbose_name = "Изображение"
    verbose_name_plural = "Изображения"
    extra = 1
    classes = ("collapsible",)
    model.__str__ = lambda self: ""


class HalfStaticPageYoutubeVideoUrlInline(admin.TabularInline):
    model = HalfStaticPageYoutubeVideoUrl
    verbose_name = "Youtube ссылка"
    verbose_name_plural = "Youtube ссылки"
    extra = 1
    classes = ("collapsible",)
    model.__str__ = lambda self: ""


@admin.register(HalfStaticPage)
class HalfStaticPageAdmin(admin.ModelAdmin):
    inlines = (
        HalfStaticPageImageInline,
        HalfStaticPageYoutubeVideoUrlInline,
    )
    list_display = ("name",)
    exclude = (
        "images",
        "slug",
    )

    def has_add_permission(self, request, obj=None):
        """Remove the save and add new button."""
        return False

    def has_delete_permission(self, request, obj=None):
        """Remove the delete button."""
        return False


@admin.register(HalfStaticPageImage)
class CarouselItemAdmin(HideOnNavPanelAdminModelMixin, admin.ModelAdmin):
    pass
