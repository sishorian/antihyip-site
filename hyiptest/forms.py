from django import forms
from django.utils.translation import gettext_lazy as _


# Forms here.
class InputDomainForm(forms.Form):
    """
    Form to ask user for a domain of the site they want to check.
    """

    domain_name = forms.RegexField(
        regex=(
            r"(?:[a-z0-9](?:[a-z0-9\-]{0,61}[a-z0-9])?\.)"
            r"+[a-z0-9][a-z0-9\-]{0,61}[a-z0-9]"
        ),
        min_length=4,  # accept short domains like t.co for now
        max_length=64,  # overkill in case 32 is too short
        strip=True,
        label="Доменное имя сайта",
        # help_text=_("Enter the site domain, like pyramid.com"),
        help_text="Введине домен сайта, например pyramid.com",
    )


class SelectAnswerForm(forms.Form):
    """
    Form to select one of the Answers of a Question.
    """

    selected_answer = forms.ModelChoiceField(
        queryset=None, label="Выберете ответ", widget=forms.RadioSelect
    )

    def __init__(self, *args, **kwargs):
        question_obj = kwargs.pop("question_obj")
        super().__init__(*args, **kwargs)
        self.fields["selected_answer"].queryset = question_obj.answer_set.all()
