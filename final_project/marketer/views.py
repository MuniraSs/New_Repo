from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import Profile


def return_home (request : HttpRequest):


  return render(request, "home.html")

#registration 
def register (request : HttpRequest):
      
      if request.method == "POST":
        #creating the user
        new_user = User.objects.create_user(username=request.POST["username"], email= request.POST["email"],  password=request.POST["password"])
        new_user.save()

        #creating the profile
        user_profile = Profile(user=new_user, age=request.POST["age"], address=request.POST["address"])
        user_profile.save()
      return render(request, "registration.html")

#login 
def login (request : HttpRequest):


  return render(request, "login.html")

def list_chances (request : HttpRequest):


  return render(request, "list_chances.html")


def add_markting_request(request : HttpRequest):


    return render(request, "add-request.html")