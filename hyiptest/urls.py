from django.urls import path

from . import views

# URLs here.
urlpatterns = [
    # Home page
    path("", views.index, name="index"),
    # Test pages
    path("tests/", views.TestSelectQGroup.as_view(), name="test_select_qgroup"),
    path(
        "test/<int:qgroup_pk>/",
        views.test_redirect_question,
        name="test_redirect_question",
    ),
    path(
        "test/<int:qgroup_pk>/<int:question_index>/",
        views.test_ask_question,
        name="test_ask_question",
    ),
]
