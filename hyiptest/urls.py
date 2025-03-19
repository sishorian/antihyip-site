from django.urls import path

from . import views

# URLs here.
urlpatterns = [
    # Home page
    path("", views.index, name="index"),
    # Test page
    path("test/", views.test_ask_question, name="test"),
]
