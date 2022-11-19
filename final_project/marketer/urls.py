from django.urls import path
from . import views

app_name = "marketer"

urlpatterns = [
    path("home/", views.return_home, name="home"),
    path("registration/", views.register, name="registration"),
    path("login/", views.login_user, name="login"),
    path("add-request/", views.add_markting_request, name="add-request"),
    path("all-requests/", views.list_chances, name="all-requests"),
    path("request_detail/<request_id>/", views.request_detail, name="request_detail"),
    path("request_detail/<request_id>/comment", views.add_comment, name="add_comment"),
    path("contact/", views.index, name="contact"),
     ] 