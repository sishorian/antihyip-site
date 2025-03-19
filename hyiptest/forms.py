from django import forms


# Forms here.
class SelectAnswerForm(forms.Form):
    """
    Form to select one of the Answers of a Question.
    """

    selected_answer = forms.ModelChoiceField(queryset=None, widget=forms.RadioSelect)

    def __init__(self, *args, **kwargs):
        question_obj = kwargs.pop("question_obj")
        super().__init__(*args, **kwargs)
        self.fields["selected_answer"].queryset = question_obj.answer_set.all()
