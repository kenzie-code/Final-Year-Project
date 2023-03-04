from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import check_password,make_password
from accounts.models import *
from .models import *
# Create your views here.

@login_required(login_url='/login/')
def home_dash(request):
    user = request.user
    profile = Customer_Details.objects.get(User__username=user)
    return render(request,'customer_dashboard/account.html',{'act1':'active','profile':profile})


@login_required(login_url='/login/')
def edit_profile(request):
    user = request.user
    profile = Customer_Details.objects.get(User__username=user)
    if request.POST:
        name = request.POST.get('name')
        email = request.POST.get('email')
        age = request.POST.get('age')
        location = request.POST.get('location')
        profile.Name = name
        profile.Age = age
        profile.Email = email
        profile.Address = location
        profile.save()
        return render(request,'customer_dashboard/editprofile.html',{'act1':'active','profile':profile,'status':'primary','message':'Profile Saved Sucessfully'})
    return render(request,'customer_dashboard/editprofile.html',{'act1':'active','profile':profile,'obj':'none'})


@login_required(login_url='/login/')
def edit_password(request):
    user = request.user
    profile = CustomUser.objects.get(username=user)
    if request.POST:
        password = request.POST.get('password')
        conf_password = request.POST.get('cpassword')
        if password == conf_password :
            profile.password = make_password(password)
            profile.save()
            return render(request,'customer_dashboard/editpassword.html',{'act1':'active','profile':profile,'status':'primary','message':'Password Saved Sucessfully'})
        return render(request,'customer_dashboard/editpassword.html',{'act1':'active','profile':profile,'status':'warning','message':'Password Mismatched'})
    return render(request,'customer_dashboard/editpassword.html',{'act1':'active','profile':profile,'obj':'none'})

@login_required(login_url='/login/')
def edit_image(request):
    user = request.user
    profile = CustomUser.objects.get(username=user)
    if request.POST:
        image = request.FILES.get('image')
        profile.profile_image = image
        profile.save()
        return render(request,'customer_dashboard/editimage.html',{'act1':'active','profile':profile,'status':'primary','message':'Profile Image Saved Sucessfully'})
    return render(request,'customer_dashboard/editimage.html',{'act1':'active','profile':profile,'obj':'none'})



def Membership_details(request):
    return render(request,'customer_dashboard/membershipdetails.html',{'act2':'active'})

def Reviews(request):
    user_n = CustomUser.objects.get(username=request.user)
    rew = Review.objects.filter(User=user_n)
    print(rew)
    val=request.GET.get("type")
    pcss = ""
    scss = ""
    if val=='See':
        dis1=''
        dis2='none'
    elif val == 'Post':
        dis1='none'
        dis2=''
        pcss = "background: #282828 ; color: white;"
        scss = "background: white ; color: #282828;"
    else:
        dis1=''
        dis2='none'
    if request.GET.get('del'):
        del_rev = Review.objects.get(id=request.GET.get('del')).delete()
        status = "warning"
        message = "Review Deleted Sucessfully"
        return render(request,'customer_dashboard/reviews.html',{'act3':'active','dis1':dis1,'dis2':dis2,'pcss':pcss,'scss':scss,'status':status,'message':message,'review':rew})
    if request.POST:
        view = request.POST.get('post_review')
        rate = request.POST.get('rating')
        username = request.POST.get('username')
        
        try :
            
            Rev = Review.objects.create(User=user_n,Rating=rate,content=view).save()
            status = 'success'
            message = 'Review Saved Sucessfully'
        except Exception as err:
            status = 'danger'
            message = 'Something Went Wrong'
        return render(request,'customer_dashboard/reviews.html',{'act3':'active','dis1':dis1,'dis2':dis2,'pcss':pcss,'scss':scss,'status':status,'message':message,'review':rew})
    return render(request,'customer_dashboard/reviews.html',{'act3':'active','dis1':dis1,'dis2':dis2,'pcss':pcss,'scss':scss,'obj':'none','review':rew})

def Products_sec(request):
    return render(request,'customer_dashboard/product_sec.html',{'act4':'active'})

def yourcart(request):
    return render(request,'customer_dashboard/yourcart.html',{'act5':'active'})
