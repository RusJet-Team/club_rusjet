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
    # fields = (
    #     "name",
    #     "short_description",
    #     "image",
    #     "image_change_page",
    #     "text",
    #     "slug",
    # )


@admin.register(ProjectCategory)
class ProjectCategoryAdmin(HideOnNavPanelAdminModelMixin, admin.ModelAdmin):
    pass


@admin.register(ProjectImage)
class CarouselItemAdmin(HideOnNavPanelAdminModelMixin, admin.ModelAdmin):
    pass
