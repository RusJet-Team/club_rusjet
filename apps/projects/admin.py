from django.contrib import admin
from django.utils.html import format_html

from apps.main_page.mixins import AdminImagePreview, HideOnNavPanelAdminModelMixin
from apps.projects.models import Project, ProjectCategory, ProjectImage


class ProjectImagesInline(admin.TabularInline):
    model = Project.images.through
    readonly_fields = ("image_preview",)
    verbose_name = "Изображение"
    verbose_name_plural = "Изображения"
    extra = 1
    classes = ("collapsible",)
    model.__str__ = lambda self: ""

    @admin.display(description="Превью изображения")
    def image_preview(self, obj):
        if obj.projectimage:
            return format_html(
                '<img src="{}" height="50" style="object-fit: contain;" />'.format(obj.projectimage.image.url)
            )


@admin.register(Project)
class Projectdmin(AdminImagePreview, admin.ModelAdmin):
    inlines = (ProjectImagesInline,)
    list_display = (
        "name",
        "category",
    )
    exclude = ("images",)
    # fields = (
    #     "name",
    #     "short_description",
    #     "image",
    #     "image_change_page",
    #     "text",
    #     "slug",
    # )


@admin.register(ProjectCategory)
class ProjectCategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(ProjectImage)
class CarouselItemAdmin(HideOnNavPanelAdminModelMixin, AdminImagePreview, admin.ModelAdmin):
    list_display = ("image_preview_list_page",)
