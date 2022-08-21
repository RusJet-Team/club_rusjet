from bootstrap_modal_forms.generic import BSModalCreateView
from django.conf import settings
from django.core.mail import send_mail
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.urls import reverse_lazy

from apps.questions.forms import QuestionModelForm
from apps.questions.models import Question


class QuestionCreateView(BSModalCreateView):
    template_name = "questions/create_question.html"
    form_class = QuestionModelForm
    success_message = "Success: Question was created."
    success_url = reverse_lazy("index")


def success_question(request):
    if request.method == "GET":
        question = Question.objects.last()
        message_data = {
            "name": question.name,
            "email": question.email,
            "phone_number": question.phone_number,
            "text": question.text,
        }
        subject = f"Поступил вопрос от {message_data.get('name')} с rusjet.ru"
        msg_plain = render_to_string("questions/email.txt", message_data)
        msg_html = render_to_string("questions/email.html", message_data)

        send_mail(
            subject,
            msg_plain,
            settings.EMAIL_HOST_USER,
            [settings.DEFAULT_FROM_EMAIL],
            html_message=msg_html,
        )

        return HttpResponse(200)
