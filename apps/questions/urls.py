from django.urls import path

from apps.questions.views import QuestionCreateView

urlpatterns = [
    path("create_question/", QuestionCreateView.as_view(), name="create_question"),
]
