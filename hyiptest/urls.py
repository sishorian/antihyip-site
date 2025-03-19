from django.urls import path

from . import views

# URLs here.
urlpatterns = [
    # Home page
    path("", views.index, name="index"),
]
