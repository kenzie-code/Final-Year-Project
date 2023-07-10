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
    if request.POST :
        try :
            name = request.POST.get('Name')
            email = request.POST.get('Email')
            contact = request.POST.get('Contact')
            message = request.POST.get('Message')
            cf = Contact_Form.objects.create(Name=name,Email=email,Contact=contact,Message=message).save()
            return render(request,"contact.html",{'info':info,'Social':Social,'status':'success','message':'Data Saved Successfully'})
        except Exception as err :
            print(err)
            return render(request,"contact.html",{'info':info,'Social':Social,'status':'danger','message':'Something Went Wrong'})
    return render(request,"contact.html",{'info':info,'Social':Social,'obj':'none'})

def Perso(request):
    info = Information.objects.latest('business_address')
    Social = social_info.objects.all()
    if request.POST :
        try :
            name = request.POST.get('Name')
            email = request.POST.get('Email')
            contact = request.POST.get('Contact')
            message = request.POST.get('Message')
            cf = Contact_Form.objects.create(Name=name,Email=email,Contact=contact,Message=message).save()
            return render(request,"contact.html",{'info':info,'Social':Social,'status':'success','message':'Data Saved Successfully'})
        except Exception as err :
            print(err)
            return render(request,"ready.html",{'info':info,'Social':Social,'status':'danger','message':'Something Went Wrong'})
    return render(request,"ready.html",{'info':info,'Social':Social,'obj':'none'})
    
    


def review(request):
    data = Review.objects.filter(verified=True)
    return render(request,'rev_page.html',{'data':data})

def job_req(request):
    info = Information.objects.latest('business_address')
    Social = social_info.objects.all()
    if request.POST:
        Name = request.POST.get('name')
        Address = request.POST.get('address')
        tex = request.POST.get('Experience')
        rex = request.POST.get('r_ex')
        mno = request.POST.get('mobilenumber')
        fb = request.POST.get('facebook')
        tw = request.POST.get('twitter')
        igt = request.POST.get('instagram')
        email = request.POST.get('email')
        sd = request.POST.get('Date')
        cv = request.FILES.get('cv')
        pic = request.FILES.get('pic')
        jr = Job_request.objects.create(Name=Name,profile_pic=pic,Email=email,Phone=mno,Address=Address,
            Recent=rex,Past=tex,facebook=fb,start_date=sd,twitter=tw,instagram=igt,cv=cv).save()
        return render(request,'job.html',{'info':info,'Social':Social,'message':'Data Saved Sucessfully','status':'success'})
    return render(request,'job.html',{'info':info,'Social':Social})



def gold_member(request):
    info = Information.objects.latest('business_address')
    Social = social_info.objects.all()
    return render(request,"gold_member.html",{'info':info,'Social':Social})

def first_timer(request):
    info = Information.objects.latest('business_address')
    Social = social_info.objects.all()
    return render(request,"firsttimer_readmore.html",{'info':info,'Social':Social})

# Concept list

def personal_training(request):
    info = Information.objects.latest('business_address')
    Social = social_info.objects.all()
    return render(request,"personal_training.html",{'info':info,'Social':Social})

def holy_booty(request):
    info = Information.objects.latest('business_address')
    Social = social_info.objects.all()
    return render(request,"holy_booty.html",{'info':info,'Social':Social})

def holy_box(request):
    info = Information.objects.latest('business_address')
    Social = social_info.objects.all()
    return render(request,"holy_box.html",{'info':info,'Social':Social})

def holy_ride(request):
    info = Information.objects.latest('business_address')
    Social = social_info.objects.all()
    return render(request,"holy_ride.html",{'info':info,'Social':Social})

def holy_shred(request):
    info = Information.objects.latest('business_address')
    Social = social_info.objects.all()
    return render(request,"holy_shred.html",{'info':info,'Social':Social})