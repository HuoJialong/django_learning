from django.urls import path
from . import views
urlpatterns = [
    path('index/', views.index),
    path('index3/', views.index3),
    path('index4/', views.index4)
]