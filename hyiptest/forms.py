from django import forms

from .models import Question


# Forms here.
class HyipTestForm(forms.Form):
    """
    Basic form for a pyramid test.
    """

    selected_answer = forms.ModelChoiceField(queryset=None, widget=forms.RadioSelect)

    def __init__(self, *args, **kwargs):
        question_pk = kwargs.pop("question_pk")
        super().__init__(*args, **kwargs)
        self.fields["selected_answer"].queryset = Question.objects.get(
            pk=question_pk
        ).answer_set.all()
