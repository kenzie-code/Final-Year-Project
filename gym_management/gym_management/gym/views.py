from django.shortcuts import render,HttpResponse
from django.contrib.auth.hashers import check_password,make_password

def home(request):
    return render(request,"index.html")

def about(request):
    return render(request,"about.html")

def pricing(request):
    return render(request,"pricing_plan.html")

def concept(request):
    return render(request,"concept.html")

def contact(request):
    return render(request,"contact.html")




