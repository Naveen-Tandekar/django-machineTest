from django.shortcuts import render,redirect
from . models import *
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages

def register_user(request):
    if request.method=="POST":
        username=request.POST["username"]
        first_name=request.POST["first_name"]
        last_name=request.POST["last_name"]
        email=request.POST["email"]
        password=request.POST["password"]
        Mobile=request.POST["Mobile"]
        age=request.POST["age"]
        Address=request.POST["Address"]
        user_data=User.objects.create_user(username=username,first_name=first_name,last_name=last_name,email=email,password=password)
        register.objects.create(user=user_data,Mobile=Mobile,age=age,Address=Address)
        return redirect("home")
    return render(request,'registered.html')

def logins(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(username=username,password=password)
        if user:
            login(request,user)
            return redirect("home")
        else:
            messages.error(request,"Username and password does not Match")
            # return redirect
    else:
        messages.info(request,"username and password does not Exist")
    return render(request,"login_page.html")

def logout(request):    
    request.session.clear()
    return redirect('home')

    

def home(request):
    return render(request,"home.html")


