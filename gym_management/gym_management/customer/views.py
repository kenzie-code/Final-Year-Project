from django.shortcuts import render,HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import check_password,make_password
from accounts.models import *
from .models import *
# Create your views here.
from django.db.models import Sum

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


@login_required(login_url='/login/')
def Membership_details(request):
    user = request.user
    member = Membership.objects.filter(User=user)
    leng = len(member)
    return render(request,'customer_dashboard/membershipdetails.html',{'act2':'active','leng':leng,'member':member})


@login_required(login_url='/login/')
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


@login_required(login_url='/login/')
def Products_sec(request):
    Prod = Product.objects.all()
    return render(request,'customer_dashboard/product_sec.html',{'act4':'active','pro':Prod})




@login_required(login_url='/login/')
def yourcart(request):
    All = cart.objects.filter(user__username=request.user)
    Len = len(All)
    total = All.aggregate(Sum('Price'))
    if request.POST:
        if request.POST.get('del'):
            Id = request.POST.get('del')
            cart_d = cart.objects.get(id=Id).delete()
            status = 'danger'
            message = 'Item removed from cart sucessfully'
        else :
            u = CustomUser.objects.get(username=request.user)
            Id = request.POST.get('id')
            Ty = request.POST.get('type') 
            pr = request.POST.get('price') 
            status = 'success'
            if Ty == "Membership":
                mem = Package.objects.get(id=Id)
                car = cart.objects.create(user=u,product_type=Ty,Member=mem,Price=pr).save()
                message = 'Membership Package added to your cart'
            else :
                mem = Product.objects.get(id=Id)
                car = cart.objects.create(user=u,product_type=Ty,Product=mem,Price=pr).save()
                message = 'Product added to your cart'
        All = cart.objects.filter(user__username=request.user)
        Len = len(All)
        total = All.aggregate(Sum('Price'))
        return render(request,'customer_dashboard/yourcart.html',{'act5':'active','status':status,'message':message,'All':All,'total_product':Len,'amount':total['Price__sum']})
    return render(request,'customer_dashboard/yourcart.html',{'act5':'active','All':All,'total_product':Len,'amount':total['Price__sum']})




