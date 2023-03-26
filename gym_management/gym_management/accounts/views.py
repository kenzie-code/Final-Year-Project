from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.hashers import check_password,make_password
from .models import *
from website.models import *
from django.contrib.auth import authenticate, login,logout
# Create your views here.


def signup(request):
    info = Information.objects.latest('business_address')
    Social = social_info.objects.all()
    if request.POST :
        username = request.POST.get('username')
        password = (request.POST.get('password'))
        cpassword = request.POST.get('cpassword')
        name = request.POST.get('name')
        email = request.POST.get('email')
        try :
            if password == cpassword:
                password = make_password(password)
                data = CustomUser.objects.create(username=username,password=password)
                data.save()
                profile = Customer_Details.objects.get(User__username=username)
                profile.Name = name
                profile.Email = email
                profile.save()
                return render(request,'Signup.html',{'message':'Profile has been created sucessfully','status':'primary','info':info,'Social':Social})
            else :
                return render(request,'Signup.html',{'message':'Password is not Matching','status':'warning','info':info,'Social':Social})

        except Exception as err :
            Err = str(err).split(':')[0]
            if Err == "UNIQUE constraint failed":
                return render(request,'Signup.html',{'message':'User is already here','status':'warning','info':info,'Social':Social})
            return render(request,'Signup.html',{'message':'Something Went Wrong','status':'danger','info':info,'Social':Social})
    return render(request,'Signup.html',{'obj':'none','info':info,'Social':Social})

def userLogin(request):
    info = Information.objects.latest('business_address')
    Social = social_info.objects.all()
    if request.POST :
        username = request.POST.get('username')
        password = (request.POST.get('password'))
        try :
            data = CustomUser.objects.get(username=username)
            if check_password(password,data.password):
                login(request,data)
                if data.user_type == 'Admin':
                    return redirect('/admin_dashboard/')
                elif data.user_type == 'Customer':
                    return redirect('/customer_dashboard/')
                else :
                    return redirect('/trainer_dashboard/')
            else :
                return render(request,'Login.html',{'message':'Incorrect Password','status':'warning','info':info,'Social':Social})
        except CustomUser.DoesNotExist:
            return render(request,'Login.html',{'message':'User is not here','status':'danger','info':info,'Social':Social})
        except Exception as err:
            print(str(err))
            return render(request,'Login.html',{'message':'Something Went Wrong','status':'danger','info':info,'Social':Social})
    return render(request,'Login.html')
        
# This is a djangi view that logs out the current user and redirects them to the homepage.
#
def userLogout(request):
    logout(request)
    return redirect('/')


# This is a simple django view that returns an HTTP response with the string 'Admin'.
# I have created a URL route in my project "gym" 'urls.py' file that maps to this view
# In this case, when a user visits the URL ''http://example.com/admin/',the 'admin_dashboard' function will be called and will 
#return an HTTP response with the string 'Admin'.
def admin_dashboard(request):
    return HttpResponse('Admin')


def trainer_dashboard(request):
    return HttpResponse('trainer_dashboard')
