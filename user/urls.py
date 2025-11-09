from django.urls import path, re_path
from . import views
urlpatterns = [
    path('index/', views.index),
    re_path(r'^info/(?P<id>\d+)/$', views.info),
    path('rev/<int:num>/', views.inbuild_reverse),
    path('rev/<str:content>/', views.inbuild_reverse2),
]