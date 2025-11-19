from django.urls import path
from . import views
urlpatterns = [
    path('software/', views.SoftwareView.as_view()),
    path('student/', views.StudentView.as_view()),
    path('student2/', views.StudentView2.as_view()),
    path('index/', views.index),
    path('index2/', views.IndexView.as_view()),
]