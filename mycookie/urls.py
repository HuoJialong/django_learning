from . import views
from django.urls import path


urlpatterns = [
    path("set_cookie/", views.set_cookie),
    path("get_cookie/", views.get_cookie),
    path("delete_cookie/", views.delete_cookie),
]