from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import Request


def return_home (request : HttpRequest):


  return render(request, "home.html")

#registration 
def register (request : HttpRequest):
      
      if request.method == "POST":
        #creating the user
        new_user = User.objects.create_user(username=request.POST["username"], email= request.POST["email"],  password=request.POST["password"])
        new_user.save()
        return redirect("marketer:login")


        #creating the profile
        #user_profile = Profile(user=new_user, age=request.POST["age"], address=request.POST["address"])
        #user_profile.save()
      return render(request, "registration.html")

#login 
def login_user (request : HttpRequest):
  msg = ""
  if request.method == "POST":
        user = authenticate(request, username=request.POST["username"], password=request.POST["password"])
        
        if user:
            login(request, user)
            return redirect("marketer:home")
        else:
            msg = "User Not Found , check your credentials"

  return render(request, "login.html", {"msg" : msg})



def list_chances (request : HttpRequest):

    req = Request.objects.all().order_by("name") #to order by name
    return render(request, "all-requests.html", {"req" : req})



def add_markting_request(request : HttpRequest):

    user : User = request.user
    msg = ""

    if not (user.is_authenticated):
       return redirect("marketer:home")
    elif  request.method == "POST":
      new_request = Request (title=request.POST["title"], name = request.POST["name"], description = request.POST["description"]  )
      msg = "Request has been sent successfully"
      new_request.save()
      #return redirect("marketer:home")
      

    return render(request, "add-request.html" , {"msg" : msg}  )

def request_detail (request : HttpRequest, request_id : int):
    try:
        req = Request.objects.get(id=request_id)
        #comments = Comment.objects.filter(post = post)
    except:
        return render(request , "not_found.html")

    return render(request, "request_detail.html", {"req" : req})




