import json

from django.conf import settings
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import render_to_string

from apps.questions.forms import QuestionModelForm


def add_question(request):
    if request.method == "POST":
        form = QuestionModelForm(request.POST)
        if form.is_valid():
            question = form.save()
            subject = f"Поступил вопрос от {form.data.get('name')} с rusjet.ru"
            msg_plain = render_to_string("questions/email.txt", form.data)
            msg_html = render_to_string("questions/email.html", form.data)
            send_mail(
                subject,
                msg_plain,
                settings.EMAIL_HOST_USER,
                [settings.DEFAULT_FROM_EMAIL],
                html_message=msg_html,
            )
            return HttpResponse(
                status=204, headers={"HX-Trigger": json.dumps({"showMessage": f"{question.name} added."})}
            )
    else:
        form = QuestionModelForm()
    return render(
        request,
        "questions/create_question.html",
        {
            "form": form,
        },
    )
