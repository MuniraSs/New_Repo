from .forms import contactForm
from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Request, Offer, Contact
from django.core.mail import send_mail
from django.template.loader import render_to_string






def index(request): 
    form_class = contactForm
    form = form_class(request.POST or None)
    if request.method == 'POST':
      
      if form.is_valid():
            email = form.cleaned_data['email']
            name = form.cleaned_data['name']
            message = form.cleaned_data['message']
            subject = form.cleaned_data['subject']

            html = render_to_string('home.html',{
              'name' : name,
              'email' : email ,
              'subject' : subject, 
              'message' : message   })
              
            send_mail('the contact from subject' , 'This is the message' , 'malsuhaim@outlook.sa',['malsuhaim@outlook.sa'], html_message=html )

            return redirect ('contact')
    else:
        form = contactForm()

    return render (request, 'contact.html', { 'form' : form })

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
      new_request = Request (title=request.POST["title"], name = request.POST["name"], description = request.POST["description"] )
      msg = "Request has been sent successfully"
      new_request.save()
      #return redirect("marketer:home")
      

    return render(request, "add-request.html" , {"msg" : msg}  )
    
def request_detail (request : HttpRequest, request_id : int):
    try:
        req = Request.objects.get(id=request_id)
        offers = Offer.objects.filter(requestt = req)
    except:
       return render(request , "not_found.html")

    return render(request, "request_detail.html", {"req" : req ,"offers" : offers }) # , 


def add_comment(request: HttpRequest, request_id:int):
    
    requestt = Request.objects.get(id=request_id)

    if request.method == "POST":
        new_comment = Offer(requestt=requestt, name = request.POST["name"], content=request.POST["content"])
        new_comment.save()

    
    return redirect("all_request.html", requestt.id)

def search(request: HttpRequest):
    
    
    if "search" in request.GET:
        posts = Request.objects.filter(title__contains=request.GET["search"])
    else:
        posts = Request.objects.all()

    return render(request, "all-requests.html", {"posts" : posts})


# contact us 

def contact_us (request : HttpRequest):
    
  if request.method == "POST":
      new_contact = Contact (name=request.POST["name"], email = request.POST["email"], subject = request.POST["subject"], message = request.POST["message"] )
      new_contact.save()
     # return redirect("marketer:contact")
      msg = " thank you ! your email has been sent"

  return render( request, "contact.html", {"msg" : msg})










