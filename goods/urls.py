from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index),
    path('hello_world/', views.hello_world),
]
