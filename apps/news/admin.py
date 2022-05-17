from django.contrib import admin

from apps.news.models import News, NewsCategory


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ("name", "pub_user")

    def save_model(self, request, obj, form, change):
        if getattr(obj, "pub_user", None) is None:
            obj.author = request.user
        obj.save()


@admin.register(NewsCategory)
class NewsCategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)
