from django.urls import path

from . import views

# URLs here.
urlpatterns = [
    # Home page
    path("", views.index, name="index"),
    # Generic views
    path("questions/", views.QuestionListView.as_view(), name="question_list"),
    path(
        "question/<int:pk>", views.QuestionDetailView.as_view(), name="question_detail"
    ),
]

# Test pages
urlpatterns += [
    path("check-domain/", views.input_domain, name="input_domain"),
    path("check-domain/<str:query>/", views.domain_result, name="domain_result"),
    path("tests/", views.SelectQGroup.as_view(), name="select_qgroup"),
    path(
        "test/<int:qgroup_pk>/",
        views.redirect_question,
        name="redirect_question",
    ),
    path(
        "test/<int:qgroup_pk>/<int:question_index>/",
        views.ask_question,
        name="ask_question",
    ),
    path("test-fail/", views.test_fail, name="test_fail"),
    path("test-pass/", views.test_pass, name="test_pass"),
]
