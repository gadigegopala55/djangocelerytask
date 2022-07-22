from urllib import request
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import *
from django.core.mail import send_mail
from celery import shared_task
from .tasks import sending_mail,sending_notification

# Create your views here.
def home(request):
    try:
        blogdata = blog.objects.all()
        return render(request,"home.html",{"blogdata":blogdata})
    except:
        return render(request,"home.html",{"blogdata":"Try again"})

#login page
def login(request):
    try:
        mydata = useradmin.objects.get()
        if mydata.userlogin == "failure":
            if request.method == "POST":
                userid = request.POST['userid']
                password = request.POST['password']
                if userid == mydata.username and password == mydata.password:
                    modify = useradmin.objects.get()
                    modify.userlogin = "success"
                    modify.save()
                    return redirect("/post")
                else:
                    return render(request,"login.html",{"message":"* Enter valid Details"})
        else:
            return redirect("/post")
        return render(request,"login.html",{"message":""})
    except:
        return render(request,"login.html",{"message" : "Try again with valid data"})

#adding a blog
def post(request):
    try:
        mydata = useradmin.objects.get()
        blogdata = blog.objects.all()
        data = mydata.userlogin
        if data == "failure":
            return redirect("/login")
        else:
            if request.method == "POST":
                title = request.POST["title"]
                description = request.POST["description"]
                if not title or not description:
                    return render(request,"post.html",{"message":"* Enter all fields", "blogdata":blogdata})

                subscriberdata = subscribers.objects.all()

                for char in subscriberdata:
                    sending_notification.delay(char.email)
                
                savedata = blog(title = title,description = description)
                savedata.save()
                return render(request,"post.html",{"message":"Successfully Posted the data", "blogdata":blogdata})
            return render(request,"post.html",{"message":"", "blogdata":blogdata})
        return redirect("/login")
    except Exception as error:
        return render(request,"post.html",{"message":error, "blogdata":blogdata})

# deleting the post
def delete(request,id):
    try:
        mydata = useradmin.objects.get()
        data = mydata.userlogin
        if data == "failure":
            return redirect("/login")
        else:
            blog.objects.filter(id = id).delete()
            return redirect("/post")
    except:
        return redirect("/post")

#Updating a post
def update(request,id):
    try:
        mydata = useradmin.objects.get()
        data = mydata.userlogin
        if data == "failure":
            return redirect("/login")
        else:
            if request.method == "POST":
                description = request.POST["description"]
                modify = blog.objects.get(id=id)
                modify.description = description
                modify.save()
                return redirect("/post")
            return render(request,"put.html")
    except:
        return render(request,"put.html")

#Logout API
def logout(request):
    try:
        modify = useradmin.objects.get()
        modify.userlogin = "failure"
        modify.save()
        return redirect("/login")
    except:
        return redirect("/login")

#Adding subcribers data
def subscribe(request):
    try:
        if request.method == "POST":
            name = request.POST['name']
            email = request.POST['email']
            phonenumber = request.POST['phonenumber']

            if not name or not email or not phonenumber:
                return render(request,"subscribe.html",{"message":"* Enter all fields"})

            sending_mail.delay(email)

            datasaving = subscribers(name=name,email=email,phonenumber=phonenumber)
            datasaving.save()
            return render(request,"subscribe.html",{"message" : "You are subscribed"})
        return render(request,"subscribe.html",{"message":""})
    except:
        return render(request,"subscribe.html",{"message":" * Enter valid Email"})

#Adding a Comment
def comment(request):
    try:
        if request.method == "POST":
            name = request.POST['name']
            comment = request.POST['comment']

            if not name or not comment:
                return render(request,"comment.html",{"message":"*Enter all fields"})
        
            commentsaving = comments(name = name, comment = comment)
            commentsaving.save()
            return render(request,"comment.html",{"message":"Commented Successfully"})
        return render(request,"comment.html",{"message":""})
    except:
        return render(request,"comment.html",{"message" : "Try again"})

#Read Comment
def readcomment(request):
    try:
        commentdata = comments.objects.all()
        return render(request,"readcomment.html",{"mydata" : commentdata})
    except:
        return render(request,"readcomment.html",{"mydata" : "Try again"})

# getting the subscription data
def subscriberslist(request):
    try:
        mydata = useradmin.objects.get()
        data = mydata.userlogin
        if data == "failure":
            return redirect("/login")
        else:
            mydata = subscribers.objects.all()
            return render(request,"subscriberslist.html",{"mydata" : mydata})
        return render(request,"subscriberslist.html",{"mydata" : mydata})
    except:
        return render(request,"subscriberslist.html",{"mydata" : "Try again"})
