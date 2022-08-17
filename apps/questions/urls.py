from django.urls import path

from apps.questions.views import QuestionCreateView, success_question

urlpatterns = [
    path("create_question/", QuestionCreateView.as_view(), name="create_question"),
    path("success-question/", success_question, name="success-question"),
]
