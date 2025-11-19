from django.urls import path
from . import views
urlpatterns = [
    path('software/',views.SoftwareView.as_view()),
    path('student/',views.StudentView.as_view()),
]