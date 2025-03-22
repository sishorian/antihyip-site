from django.http import Http404, HttpResponseBadRequest
from django.shortcuts import get_object_or_404, redirect, render
from django.views import generic

from .forms import SelectAnswerForm
from .models import QGroup


# Create your views here.
def index(request):
    return render(request, "index.html")


class SelectQGroup(generic.ListView):
    model = QGroup
    template_name = "hyiptest/select_qgroup.html"


def redirect_question(request, qgroup_pk):
    """
    Takes the selected QGroup and redirects user to the first question.
    Also responsible for setting the test score/flag.
    """

    qgroup = get_object_or_404(QGroup, pk=qgroup_pk)
    if not list(qgroup.questions.all()):
        raise Http404(f"QGroup {qgroup_pk} doesn't have any questions.")
    request.session["fail_score"] = 0

    return redirect("ask_question", qgroup_pk=qgroup_pk, question_index=0)


def ask_question(request, qgroup_pk, question_index):
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
    qgroup_len = len(qgroup_questions)
    if "fail_score" not in request.session:
        return HttpResponseBadRequest(
            "No fail_score value was provided.".encode(encoding="utf-8")
        )

    if request.method != "POST":  # to suppress "possibly unbound" error for form
        form = SelectAnswerForm(question_obj=current_question)
    else:
        form = SelectAnswerForm(request.POST, question_obj=current_question)
        while True:  # should not loop, run just once
            if not form.is_valid():
                break

            request.session["fail_score"] += form.cleaned_data[
                "selected_answer"
            ].bad_score
            if question_index < qgroup_len - 1:  # i < last
                return redirect(
                    "ask_question",
                    qgroup_pk=qgroup_pk,
                    question_index=question_index + 1,
                )
            if request.session["fail_score"] >= 16:
                return redirect("test_fail")
            return redirect("test_pass")  # break

    context = {
        "form": form,
        "question_ordinal": question_index + 1,
        "num_questions": qgroup_len,
        "question": current_question,
        "fail_score": request.session["fail_score"],
    }
    return render(request, "hyiptest/ask_question.html", context)


def test_fail(request):
    return render(request, "hyiptest/test_fail.html")


def test_pass(request):
    return render(request, "hyiptest/test_pass.html")
