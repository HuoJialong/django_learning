from django.urls import path

from modeldemo import views

urlpatterns = [
      path('user/', views.UserView.as_view()),
]