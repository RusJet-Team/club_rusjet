from django.contrib import admin

from apps.questions.models import Question


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ("name", "email")

    def has_add_permission(self, request, obj=None):
        """Remove the save and add new button."""
        return False
