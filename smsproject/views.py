from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render

def demofunction(request):
    return HttpResponse("<h2 align=center>PFSD SDP PROJECT")

def demofunction1(request):
    return HttpResponse("<h3>KL UNIVERSITY</h1>")

def demofunction2(request):
    return HttpResponse("<font color='red'>STUDENT ACADEMIC REGISTRATION SYSTEM</font>")

def homefunction(request):
    return render(request,"index.html")

def aboutfunction(request):
    return render(request,"about.html")

def loginfunction(request):
    return render(request,"login.html")

def contactfunction(request):
    return render(request,"contact.html")


