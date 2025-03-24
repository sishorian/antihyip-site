from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404, HttpResponseBadRequest
from django.shortcuts import get_object_or_404, redirect, render
from django.views import generic

from .forms import InputDomainForm, SelectAnswerForm
from .models import BadSite, QGroup, Question


# Create your views here.
def index(request):
    return render(request, "index.html")


class QuestionListView(generic.ListView):
    model = Question
    paginate_by = 20


class QuestionDetailView(generic.DetailView):
    model = Question


class BadSiteListView(generic.ListView):
    model = BadSite
    paginate_by = 20


class BadSiteDetailView(generic.DetailView):
    model = BadSite


def input_domain(request):
    """
    Asks user for a domain of the site they want to check.
    """

    if request.method == "GET":
        form = InputDomainForm()
    elif request.method == "POST":
        form = InputDomainForm(request.POST)
        if form.is_valid():
            return redirect(
                "domain_result",
                # According to the doc, should be a string.
                # form.cleaned_data[ "domain_name" ].lower(),
                # Should be lowercase because of the RegexField regex string.
                form.cleaned_data["domain_name"],
            )

    context = {
        "form": form,  # pyright: ignore[reportPossiblyUnboundVariable]
    }
    return render(request, "hyiptest/input_domain.html", context)


def domain_result(request, query):
    """
    Check the provided domain for matches in the database
    and show the result to the user.
    """
    # query should be already lowercase.
    """
    # Locate multiple domains using a substring.
    found_sites_queryset = BadSite.objects.filter(domain__contains=query)
    context = {
        "found_sites_queryset": found_sites_queryset,
    }
    """
    # Locate the exact domain using an exact string.
    try:
        found_site = BadSite.objects.get(domain__exact=query)
    except ObjectDoesNotExist:
        found_site = None
    context = {
        "found_site": found_site,
    }
    return render(request, "hyiptest/domain_result.html", context)


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

    qgroup = get_object_or_404(QGroup, pk=qgroup_pk)
    qgroup_questions = qgroup.questions.all()
    qgroup_len = len(qgroup_questions)

    try:
        current_question = qgroup_questions[question_index]
    except IndexError:
        raise Http404(
            f"QGroup {qgroup_pk} doesn't have a question under index {question_index}."
        )
    if "fail_score" not in request.session:
        return HttpResponseBadRequest(
            "No fail_score value was provided.".encode(encoding="utf-8")
        )

    if request.method == "GET":
        form = SelectAnswerForm(question_obj=current_question)
    elif request.method == "POST":
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
            if request.session["fail_score"] >= qgroup.fail_floor:
                return redirect("test_fail")
            return redirect("test_pass")  # break

    context = {
        "form": form,  # pyright: ignore[reportPossiblyUnboundVariable]
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
