
from . import views
from django.urls import path


urlpatterns = [
    path("Student/", views.StudentView.as_view()),
    path("article/", views.ArticleView.as_view()),
    path("teacher/", views.TeacherView.as_view()),
    path("area/", views.AreaView.as_view()),
]