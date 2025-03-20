from django.http import Http404
from django.shortcuts import get_object_or_404, redirect, render
from django.views import generic

from .forms import SelectAnswerForm
from .models import QGroup


# Create your views here.
def index(request):
    return render(request, "index.html")


class TestSelectQGroup(generic.ListView):
    model = QGroup
    template_name = "hyiptest/test_select_qgroup.html"


def test_redirect_question(request, qgroup_pk):
    """
    Takes the selected QGroup and redirects user to the first question.
    """

    qgroup = get_object_or_404(QGroup, pk=qgroup_pk)
    if not list(qgroup.questions.all()):
        raise Http404(f"QGroup {qgroup_pk} doesn't have any questions.")

    return redirect("test_ask_question", qgroup_pk=qgroup_pk, question_index=0)


def test_ask_question(request, qgroup_pk, question_index):
    """
    View for asking a user a Question
    and letting him to choose one of its Answers.
    """

    qgroup_questions = get_object_or_404(QGroup, pk=qgroup_pk).questions.all()
    try:
        current_question = qgroup_questions[question_index]
    except IndexError:
        raise Http404(
            f"QGroup {qgroup_pk} doesn't have a question under index {question_index}."
        )

    if request.method == "POST":
        form = SelectAnswerForm(request.POST, question_obj=current_question)
        if (
            form.is_valid()
            and form.cleaned_data["selected_answer"].bad_absolute is True
        ):
            return redirect("test_fail")
        elif form.is_valid() and question_index < (len(qgroup_questions) - 1):
            return redirect(
                "test_ask_question",
                qgroup_pk=qgroup_pk,
                question_index=question_index + 1,
            )
        elif form.is_valid():
            return redirect("test_pass")
    else:
        form = SelectAnswerForm(question_obj=current_question)

    context = {
        "form": form,
        "question": current_question,
    }
    return render(request, "hyiptest/test_ask_question.html", context)


def test_fail(request):
    return render(request, "hyiptest/test_fail.html")


def test_pass(request):
    return render(request, "hyiptest/test_pass.html")
