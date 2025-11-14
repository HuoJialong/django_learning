
from . import views
from django.urls import path


urlpatterns = [
    path("Student/", views.StudentView.as_view()),
]