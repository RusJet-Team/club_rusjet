from django import forms

from apps.questions.models import Question


class QuestionModelForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ["name", "email", "phone_number", "text"]
