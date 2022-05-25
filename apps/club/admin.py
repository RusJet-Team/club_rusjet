from django.contrib import admin
from django.utils.html import format_html

from apps.club.models import ClubMember, HalfStaticPage, HalfStaticPageImage
from apps.main_page.mixins import AdminImagePreview, HideOnNavPanelAdminModelMixin


@admin.register(ClubMember)
class ClubMemberAdmin(AdminImagePreview, admin.ModelAdmin):
    list_display = (
        "vocation",
        "image_preview_list_page",
    )
    readonly_fields = ("image_preview_change_page",)


class HalfStaticPageImageInline(admin.TabularInline):
    model = HalfStaticPage.images.through
    readonly_fields = (
        "image_preview",
        "image_url",
    )
    verbose_name = "Изображение"
    verbose_name_plural = "Изображения"
    extra = 1
    classes = ("collapsible",)
    model.__str__ = lambda self: ""

    @admin.display(description="Превью изображения")
    def image_preview(self, obj):
        if obj.halfstaticpageimage:
            print(dir(obj.halfstaticpageimage.image))
            return format_html(
                '<img src="{}" height="50" style="object-fit: contain;" />'.format(obj.halfstaticpageimage.image.url)
            )

    @admin.display(description="Ссылка для вставки в редактор")
    def image_url(self, obj):
        if obj.halfstaticpageimage:
            return format_html(
                f'<a href="{obj.halfstaticpageimage.image.url}">Ссылка</a>'
                f"<br /><a>Скопируйте и вставьте в редактор</a>"
            )


@admin.register(HalfStaticPage)
class HalfStaticPageAdmin(admin.ModelAdmin):
    inlines = (HalfStaticPageImageInline,)
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
