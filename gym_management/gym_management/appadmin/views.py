from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import check_password,make_password
from accounts.models import *
# Create your views here.

@login_required(login_url='/login/')
def home_dash(request):
    cu = CustomUser.objects.filter(user_type='Customer')
    cut = CustomUser.objects.filter(user_type='Trainer')
    member = len(cu)
    trainer = len(cut)
    return render(request,'admin_dashboard/account.html',{'act':'active','member':member,'trainer':trainer})

@login_required(login_url='/login/')
def editpassword(request):
    user = request.user
    profile = CustomUser.objects.get(username=user)
    if request.POST:
        password = request.POST.get('password')
        conf_password = request.POST.get('cpassword')
        if password == conf_password :
            profile.password = make_password(password)
            profile.save()
            return render(request,'admin_dashboard/edit_password.html',{'act':'active','status':'primary','message':'Password Saved Sucessfully'})
        return render(request,'admin_dashboard/edit_password.html',{'act':'active','status':'warning','message':'Password Mismatched'})
    return render(request,'admin_dashboard/edit_password.html',{'act':'active'})

@login_required(login_url='/login/')
def trainer_details(request):
    return render(request,'admin_dashboard/trainer_details.html',{'act1':'active'})

@login_required(login_url='/login/')
def edit_trainer(request):
    return render(request,'admin_dashboard/edit_trainer.html',{'act1':'active'})

@login_required(login_url='/login/')
def add_trainer(request):
    return render(request,'admin_dashboard/add_trainer.html',{'act1':'active'})

@login_required(login_url='/login/')
def job_request(request):
    return render(request,'admin_dashboard/job_request.html',{'act6':'active'})

@login_required(login_url='/login/')
def Members_details(request):
    return render(request,'admin_dashboard/membersdetails.html',{'act2':'active'})

@login_required(login_url='/login/')
def edit_member(request):
    return render(request,'admin_dashboard/edit_member.html',{'act2':'active'})   

@login_required(login_url='/login/')
def Reviews(request):
    val=request.GET.get("type")
    print(val)
    if val=='See':
        dis1=''
        dis2='none'
    elif val == 'Post':
        dis1='none'
        dis2=''
    else:
        dis1=''
        dis2='none'
    return render(request,'admin_dashboard/reviews.html',{'act3':'active','dis1':dis1,'dis2':dis2})

@login_required(login_url='/login/')
def Products_sec(request):
    return render(request,'admin_dashboard/product_sec.html',{'act4':'active'})

@login_required(login_url='/login/')
def add_product(request):
    return render(request,'admin_dashboard/add_product.html',{'act4':'active'})

@login_required(login_url='/login/')
def payment(request):
    return render(request,'admin_dashboard/payment.html',{'act5':'active'})
