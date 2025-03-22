from django.urls import path

from . import views

# URLs here.
urlpatterns = [
    # Home page
    path("", views.index, name="index"),
    # Test pages
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
