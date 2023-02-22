from django.shortcuts import render,HttpResponse
from django.contrib.auth.hashers import check_password,make_password
from .models import *
# Create your views here.


def home(request):
    return render(request,'index.html')

def signup(request):
    if request.POST :
        username = request.POST.get('username')
        password = make_password(request.POST.get('password'))
        name = request.POST.get('name')
        email = request.POST.get('email')
        try :
            data = CustomUser.objects.create(username=username,password=password)
            data.save()
            profile = Customer_Details.objects.get(User__username=username)
            profile.Name = name
            profile.Email = email
            profile.save()
            return render(request,'Signup.html',{'message':'Profile has been created sucessfully','status':'primary'})
        except Exception as err :
            Err = str(err).split(':')[0]
            if Err == "UNIQUE constraint failed":
                return render(request,'Signup.html',{'message':'User is already here','status':'warning'})
            return render(request,'Signup.html',{'message':'Something Went Wrong','status':'danger'})
    return render(request,'Signup.html',{'obj':'none'})

def login(request):
    if request.POST :
        username = request.POST.get('username')
        password = (request.POST.get('password'))
        try :
            data = CustomUser.objects.get(username=username)
            if check_password(password,data.password):
                return HttpResponse('Login Sucessful')
            else :
                return render(request,'Login.html',{'message':'Incorrect Password','status':'warning'})
        except CustomUser.DoesNotExist:
            return render(request,'Login.html',{'message':'User is not here','status':'danger'})
        except Exception:
            return render(request,'Login.html',{'message':'Something Went Wrong','status':'danger'})
    return render(request,'Login.html')
        

def admin_dashboard(request):
    return HttpResponse()

def customer_dashboard(request):
    return HttpResponse('customer_dashboard')

def trainer_dashboard(request):
    return HttpResponse('trainer_dashboard')
