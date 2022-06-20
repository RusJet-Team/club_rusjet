from django.contrib import admin

from apps.main_page.mixins import AdminImagePreview
from apps.news.models import News, NewsCategory


@admin.register(News)
class NewsAdmin(AdminImagePreview, admin.ModelAdmin):
    list_display = ("name", "get_news_author", "pub_date", "image_preview_list_page")
    readonly_fields = ("pub_date", "get_news_author", "image_preview_change_page")
    list_filter = ("category", "event_date")
    search_fields = (
        "name",
        "title",
        "text",
        "category__name",
    )
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "name",
                    "title",
                    "text",
                    "category",
                    "image",
                    "image_preview_change_page",
                    "event_bool",
                    "get_news_author",
                    "pub_date",
                ),
            },
        ),
        (
            None,
            {
                "fields": (
                    "event_date",
                    "geolocation_url",
                ),
                "classes": ("form-row field-event_bool",),
            },
        ),
    )
    ordering = ("-pub_date",)

    def save_model(self, request, obj, form, change):
        if getattr(obj, "pub_user", None) is None:
            obj.pub_user = request.user
        obj.save()

    @admin.display(description="Автор новости")
    def get_news_author(self, obj):
        if obj.pub_user:
            return f"{obj.pub_user.first_name} {obj.pub_user.last_name}"

    class Media:

        js = ("admin/news/js/NewsEvent.js",)


@admin.register(NewsCategory)
class NewsCategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)
