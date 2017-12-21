from django.shortcuts import render, redirect
from .models import * 
from django.contrib import messages 
from datetime import date,datetime
def index(request):
    return render(request, "blackBelt_app/index.html")

def register(request): 
    response = User.objects.register(
        request.POST["first"],
        request.POST["username"],
        request.POST["password"], 
        request.POST["confirm"]
    )
    if response["valid"]: 
        request.session["user_id"] = response["user"].id 
        return redirect("/")
    else: 
        for error_message in response["errors"]: 
            messages.add_message(request, messages.ERROR, error_message)
        return redirect("/")

def login(request): 
    response = User.objects.login(
        request.POST["username"],
        request.POST["password"]
    )
    if response["valid"]: 
        request.session["user_id"] = response["user"].id 
        return redirect("/travels")
    else: 
        for error_message in response["errors"]: 
            messages.add_message(request, messages.ERROR, error_message)
        return redirect("/")

def home(request): 
    if "user_id" not in request.session: 
        return redirect("/")
    user = User.objects.get(id=request.session["user_id"])
    trips = Trip.objects.exclude(users=user).exclude(created_by=user)
    us = Trip.objects.filter(users = user)
    er = Trip.objects.filter(created_by =user)
    userstrip = us | er
    print userstrip
    return render(request, "blackBelt_app/home.html" , {"user" : user,'trips' : trips, 'userstrip': userstrip})

def logout(request): 
    request.session.clear()
    return redirect("/")

def create(request):
    return render(request, "blackBelt_app/trip.html")

def add(request):
    response = { 
        "errors" : [],
        "user" : request.session["user_id"]
    }
    print request.POST
    dest = request.POST.get("place","")
    disc = request.POST.get("disc","")
    start= str(request.POST.get("start",""))
    end = str(request.POST.get("end",""))
    if len(dest)<1:
       response['errors'].append("Destination is required!")
    if len(disc)<1:
       response['errors'].append("Discription is required!")
    if len(start)<1:
        response["errors"].append("start date is required!") 
    if len(start)>0:
        start =  datetime.strptime(request.POST.get("start",""),'%Y-%m-%d') 
        if start < datetime.today():
            response["errors"].append("start date must be in future!")
    if len(end)<1:
        response["errors"].append("end date is required!")
    if len(end)>0:
        end =  datetime.strptime(request.POST.get("end",""),'%Y-%m-%d')
        if end < start:
            response["errors"].append("end date must be afer start!")
    if len(response["errors"])>0:
        for error_message in response["errors"]: 
            messages.add_message(request, messages.ERROR, error_message)
        return redirect("/travels/add")
    else:
        Trip.objects.create(destination=dest,description=disc,start_date=start,end_date=end,created_by=user)
        return redirect("/travels")

def user(request,number):
    user = User.objects.get(id=number)
    return render(request, "blackBelt_app/user.html", {"user": user})

def destination(request,number):
    trip = Trip.objects.get(id=number)
    return render(request, "blackBelt_app/place.html", {"trip": trip})

def join(request,number):
    this_trip= Trip.objects.get(id=number)
    this_user= User.objects.get(id=request.session["user_id"])
    this_trip.users.add(this_user)
    return redirect("/travels")
