from django import forms
from django.core.exceptions import ValidationError
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
        # max_length=64,  # if using CharField
        strip=True,
        label="Доменное имя сайта",
        # help_text=_("Enter the site domain, like pyramid.com"),
        help_text="Введине домен сайта, например pyramid.com",
    )

    def clean_domain_name(self):
        data = self.cleaned_data["domain_name"]

        # Accept short domains like t.co for now
        if len(data) < 4:
            raise ValidationError(_("Domain name too short"))

        # Overkill in case 32 is too short
        if len(data) > 64:
            raise ValidationError(_("Domain name too long"))

        return data


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
