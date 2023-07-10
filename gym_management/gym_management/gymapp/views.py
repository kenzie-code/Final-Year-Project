from django.shortcuts import render
from .models import *
from appadmin.models import *
from customer.models import *
# Create your views here.
from django.shortcuts import render

def home(request):
    images = Gallery.objects.all()
    info = Information.objects.latest('business_address')
    cd = cards.objects.all()
    upcard = headline_cards.objects.all()
    Social = social_info.objects.all()
    rew = Review.objects.filter(bookmarked=True)
    return render(request,"index.html",{'images':images,'info':info,'cards':cd,'upcard':upcard,'Social':Social,'rew':rew})
