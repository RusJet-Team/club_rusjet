from bootstrap_modal_forms.generic import BSModalCreateView
from django.http import HttpResponse
from django.urls import reverse_lazy

from apps.questions.forms import QuestionModelForm


class QuestionCreateView(BSModalCreateView):
    template_name = "questions/create_question.html"
    form_class = QuestionModelForm
    success_message = "Success: Question was created."
    success_url = reverse_lazy("index")


def success_question(request):
    if request.method == "GET":
        return HttpResponse(200)
