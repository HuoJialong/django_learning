from django.urls import path
from . import views

urlpatterns = [
    path('index6/', views.index6),
    path('index5/', views.index5),
    path('index7/', views.index7),
    path('user/', views.user),
    path('home/', views.home),
    path("get_img/", views.get_img),
]