from django.shortcuts import render
from .models import *
from appadmin.models import *
# Create your views here.
from django.shortcuts import render

def home(request):
    images = Gallery.objects.all()
    info = Information.objects.latest('business_address')
    cd = cards.objects.all()
    upcard = headline_cards.objects.all()
    Social = social_info.objects.all()
    return render(request,"index.html",{'images':images,'info':info,'cards':cd,'upcard':upcard,'Social':Social})

def about(request):
    info = Information.objects.latest('business_address')
    Social = social_info.objects.all()
    return render(request,"about.html",{'info':info,'Social':Social})

def pricing(request):
    plan = Package.objects.all().exclude(Type__Name='Workout')
    workout = Package.objects.filter(Type__Name='Workout')
    info = Information.objects.latest('business_address')
    Social = social_info.objects.all()
    return render(request,"pricing_plan.html",{'plan':plan,'workout':workout,'info':info,'Social':Social})

def concept(request):
    info = Information.objects.latest('business_address')
    Social = social_info.objects.all()
    return render(request,"concept.html",{'info':info,'Social':Social})

def contact(request):
    info = Information.objects.latest('business_address')
    Social = social_info.objects.all()
    return render(request,"contact.html",{'info':info,'Social':Social})

def gold(request):
    info = Information.objects.latest('business_address')
    Social = social_info.objects.all()
    return render(request, "gold_member.html", {'info':info,'Social':Social})





