from django.shortcuts import render

from .forms import SelectAnswerForm
from .models import Question


# Create your views here.
def index(request):
    return render(request, "index.html")


from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.urls import reverse


def test_ask_question(request):
    """
    View for asking a user a Question
    and letting him to choose one of its Answers.
    """

    pk = 1
    question = get_object_or_404(Question, pk=pk)

    if request.method == "POST":
        form = SelectAnswerForm(request.POST, question_obj=question)
        if form.is_valid():
            return HttpResponseRedirect(reverse("index"))
    else:
        form = SelectAnswerForm(question_obj=question)

    context = {
        "form": form,
        "question": question,
    }
    return render(request, "hyiptest/test_ask_question.html", context)
