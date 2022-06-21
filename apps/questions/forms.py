from bootstrap_modal_forms.forms import BSModalModelForm

from apps.questions.models import Question


class QuestionModelForm(BSModalModelForm):
    class Meta:
        model = Question
        fields = ["name", "email", "text"]
