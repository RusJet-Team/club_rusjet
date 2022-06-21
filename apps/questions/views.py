from bootstrap_modal_forms.generic import BSModalCreateView
from django.urls import reverse_lazy

from apps.questions.forms import QuestionModelForm


class QuestionCreateView(BSModalCreateView):
    template_name = "questions/create_question.html"
    form_class = QuestionModelForm
    success_message = "Success: Book was created."
    success_url = reverse_lazy("index")
