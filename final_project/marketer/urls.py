from django.urls import path
from . import views

app_name = "marketer"

urlpatterns = [
    path("home/", views.return_home, name="home"),
    path("list_chances/", views.list_chances, name="list_chances"),
    path("markting_request/", views.add_markting_request, name="add_markting_request"),
    path("registration/", views.register, name="registration"),
    path("login/", views.login, name="login"),
    path("add-request/", views.add_markting_request, name="add-request"),
    path("all-requests/", views.list_chances, name="all-requests") ] 