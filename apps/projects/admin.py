from django.contrib import admin

from apps.main_page.mixins import AdminImagePreview, HideOnNavPanelAdminModelMixin
from apps.projects.models import Project, ProjectCategory, ProjectImage


class ProjectImagesInline(AdminImagePreview, admin.TabularInline):
    model = ProjectImage
    readonly_fields = ("image_preview",)
    verbose_name = "Изображение"
    verbose_name_plural = "Изображения"
    extra = 1
    classes = ("collapsible",)
    model.__str__ = lambda self: ""


@admin.register(Project)
class ProjectAdmin(AdminImagePreview, admin.ModelAdmin):
    inlines = (ProjectImagesInline,)
    list_display = (
        "name",
        "category",
    )
    exclude = ("images",)
    list_filter = ("category",)
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "name",
                    "category",
                    "title",
                    "text",
                ),
            },
        ),
    )
    search_fields = (
        "name",
        "title",
    )


@admin.register(ProjectCategory)
class ProjectCategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(ProjectImage)
class CarouselItemAdmin(HideOnNavPanelAdminModelMixin, admin.ModelAdmin):
    pass
