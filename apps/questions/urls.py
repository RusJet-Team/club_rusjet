from django.urls import path

from apps.questions.views import add_question

urlpatterns = [
    path("ask_question", add_question, name="ask_question"),
]
