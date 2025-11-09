from django.urls import path
from . import views

urlpatterns = [
    # 类视图的绑定方式，
    # path('路径/', views.类视图名.as_view()),
    path('user/', views.UserView.as_view()),
    path("formview/", views.FormView.as_view()),
]