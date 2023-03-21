from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import check_password,make_password
from accounts.models import *
from .models import *
from customer.models import *
# Create your views here.

@login_required(login_url='/login/')
def home_dash(request):
    cu = CustomUser.objects.filter(user_type='Customer')
    cut = CustomUser.objects.filter(user_type='Trainer')
    prize = Customer_Details.objects.all().order_by('-id')[:4]
    member = len(cu)
    trainer = len(cut)
    return render(request,'admin_dashboard/account.html',{'act':'active','member':member,'trainer':trainer,'prize':prize})

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
    trainer = Trainer_Details.objects.all()
    return render(request,'admin_dashboard/trainer_details.html',{'act1':'active','trainers':trainer})

@login_required(login_url='/login/')
def edit_trainer(request):
    return render(request,'admin_dashboard/edit_trainer.html',{'act1':'active'})

@login_required(login_url='/login/')
def add_trainer(request):
    return render(request,'admin_dashboard/add_trainer.html',{'act1':'active'})

@login_required(login_url='/login/')
def job_request(request):
    profile = Job_request.objects.all()
    if request.GET.get('id'):
        jr = Job_request.objects.get(id=request.GET.get('id')).delete()
        return render(request,'admin_dashboard/job_request.html',{'act6':'active','profile':profile,'status':'danger','message':'Request Deleted Sucessfully'})
    elif request.GET.get('hire') == True or request.GET.get('hire') == 'True':
        return render(request,'admin_dashboard/job_request.html',{'act6':'active','profile':profile,'status':'success','message':'Trainer Hired Sucessfully'})
    return render(request,'admin_dashboard/job_request.html',{'act6':'active','profile':profile,'obj':'none'})

@login_required(login_url='/login/')
def Members_details(request):
    members = Customer_Details.objects.all()
    if request.GET.get('del')==True or request.GET.get('del')=='True':
        return render(request,'admin_dashboard/membersdetails.html',{'act2':'active','members':members,'message':'Member Profile has been deleted sucessfully'})
    return render(request,'admin_dashboard/membersdetails.html',{'act2':'active','members':members,'obj':'none'})

@login_required(login_url='/login/')
def edit_member(request):
    Id = request.GET.get('id')
    cus = Customer_Details.objects.get(id=Id)
    pack = Package.objects.all()
    trainer = Trainer_Details.objects.all()
    if request.POST:
        packa = request.POST.get('pack')
        train = request.POST.get('train')
        location = request.POST.get('location')
        packa = Package.objects.get(id=packa)
        train = CustomUser.objects.get(id=train)
        cus.Package = packa
        cus.Trainer = train
        cus.Address = location
        cus.save()
        tra = Trainer_Details.objects.get(User=train)
        tra.Customer.add(cus)
        tra.save()
        return render(request,'admin_dashboard/edit_member.html',{'act2':'active','cus':cus,'pack':pack,'trainer':trainer,'status':'success','message':'Member Profile has been updated sucessfully'})
    return render(request,'admin_dashboard/edit_member.html',{'act2':'active','cus':cus,'pack':pack,'trainer':trainer})   

@login_required(login_url='/login/')
def Reviews(request):
    reviews = Review.objects.all()
    try :
        if request.GET.get('del'):
            rew = Review.objects.get(id=request.GET.get('del')).delete()
            status = 'warning'
            message = 'Review Deleted Sucessfully'
            return render(request,'admin_dashboard/reviews.html',{'act3':'active','reviews':reviews})
        elif request.GET.get('bookmark'):
            rew = Review.objects.get(id=request.GET.get('bookmark'))
            rew.bookmarked = True
            rew.save()
            status = 'info'
            message = 'Bookmarked Sucessfully'
            return render(request,'admin_dashboard/reviews.html',{'act3':'active','reviews':reviews,'message':message,'status':status})
        elif request.GET.get('verify'):
            rew = Review.objects.get(id=request.GET.get('verify'))
            rew.verified = True
            rew.save()
            status = 'success'
            message = 'Verified Sucessfully'
            return render(request,'admin_dashboard/reviews.html',{'act3':'active','reviews':reviews,'message':message,'status':status})
    except Exception as err:
        print(err)
        message = 'Something Went Wrong'
        status = 'danger'
        return render(request,'admin_dashboard/reviews.html',{'act3':'active','reviews':reviews,'message':message,'status':status})
    return render(request,'admin_dashboard/reviews.html',{'act3':'active','reviews':reviews})

@login_required(login_url='/login/')
def Products_sec(request):
    pro = Product.objects.all()
    if request.POST :
        Id = request.POST.get('Id')
        data = Product.objects.get(id=Id).delete()
        return render(request,'admin_dashboard/product_sec.html',{'act4':'active','pro':pro,'message':'Product has been deleted sucessfully'})
    return render(request,'admin_dashboard/product_sec.html',{'act4':'active','pro':pro,'obj':'none'})

@login_required(login_url='/login/')
def Package_list(request):
    pack = Package.objects.all()
    if request.GET.get('del'):
        Id = request.GET.get('del')
        data = Package.objects.get(id=Id)
        data.delete()
        return render(request,'admin_dashboard/package.html',{'act7':'active','pack':pack,'status':'danger','message':'Package Deleted Sucessfully'})
    return render(request,'admin_dashboard/package.html',{'act7':'active','pack':pack,'obj':'none'})


@login_required(login_url='/login/')
def edit_package(request):
    Id = request.GET.get('id')
    pack = Package.objects.get(id=Id)
    Ty = Type.objects.all()
    if request.POST:
        Name = request.POST.get('Name')
        theme = request.POST.get('theme')
        Description = request.POST.get('Description')
        Message = request.POST.get('Message')
        Duration = request.POST.get('Duration')
        type = request.POST.get('type')
        Price = request.POST.get('Price')
        pack.Name = Name
        pack.Price = Price
        typ = Type.objects.get(Name=type)
        pack.Type = typ
        pack.Description = Description
        pack.Duration = Duration
        pack.Message = Message
        pack.theme=theme
        pack.save()
        return render(request,'admin_dashboard/edit_package.html',{'act7':'active','pack':pack,'message':'Data Saved Sucessfully','Ty':Ty})
    return render(request,'admin_dashboard/edit_package.html',{'act7':'active','pack':pack,'obj':'none','Ty':Ty})


@login_required(login_url='/login/')
def add_package(request):
    Ty = Type.objects.all()
    if request.POST:
        Name = request.POST.get('Name')
        theme = request.POST.get('theme')
        Description = request.POST.get('Description')
        Message = request.POST.get('Message')
        Duration = request.POST.get('Duration')
        type = request.POST.get('type')
        Price = request.POST.get('Price')
        typ = Type.objects.get(Name=type)
        pack = Package.objects.create(Name = Name,Price = Price,Type = typ,Description = Description,Duration = Duration,Message = Message,theme=theme)
        pack.save()
        return render(request,'admin_dashboard/add_package.html',{'act7':'active','status':'success','message':'Data Saved Sucessfully','Ty':Ty})
    return render(request,'admin_dashboard/add_package.html',{'act7':'active','obj':'none','Ty':Ty})



@login_required(login_url='/login/')
def add_product(request):
    cat = Category.objects.all()
    if request.POST:
        try :
            Product_Name = request.POST.get("product_name")
            Quantity = request.POST.get("product_quant")
            Price = request.POST.get("price")
            Product_id = request.POST.get("product_id")
            Droping_Price = request.POST.get("drop_price")
            Product_Description = request.POST.get("desc")
            Product_Category = request.POST.get("product_cat")
            Product_Category = Category.objects.get(id=Product_Category)
            Product_Tag_1 = request.POST.get("product_tag1")
            Product_Tag_2 = request.POST.get("product_tag2")
            Product_Tag_3 = request.POST.get("product_tag3")
            Product_Image = request.FILES.get("product_image")
            pro = Product.objects.create(Product_id=Product_id,Product_Name=Product_Name,Quantity=Quantity,Price=Price,
                Droping_Price=Droping_Price,Product_Description=Product_Description,Product_Category=Product_Category,
                Product_Tag_1=Product_Tag_1,Product_Tag_2=Product_Tag_2,Product_Tag_3=Product_Tag_3,Product_Image=Product_Image).save()
            message = 'Product Created Sucessfully'
            status = 'success'
        except Exception :
            message = 'Product Not Created'
            status = 'warning'
        return render(request,'admin_dashboard/add_product_.html',{'act4':'active','message':message,'status':status})
    return render(request,'admin_dashboard/add_product_.html',{'act4':'active','obj':'none',"cat":cat})

@login_required(login_url='/login/')
def Products_edit(request):
    Id = request.GET.get('id')
    pro = Product.objects.get(id=Id)
    cat = Category.objects.all()
    if request.POST:
        try :
            Product_id = request.POST.get("Product_id")
            Product_Name = request.POST.get("product_name")
            Quantity = request.POST.get("product_quant")
            Price = request.POST.get("price")
            Droping_Price = request.POST.get("drop_price")
            Product_Description = request.POST.get("desc")
            Product_Category = request.POST.get("product_cat")
            Product_Category = Category.objects.get(id=Product_Category)
            Product_Tag_1 = request.POST.get("product_tag1")
            Product_Tag_2 = request.POST.get("product_tag2")
            Product_Tag_3 = request.POST.get("product_tag3")
            Product_Image = request.FILES.get("product_image")
            pro.Quantity=Quantity
            pro.Price=Price
            pro.Droping_Price=Droping_Price
            pro.Product_Description=Product_Description
            pro.Product_Category=Product_Category
            pro.Product_Tag_1=Product_Tag_1
            pro.Product_Tag_2=Product_Tag_2
            pro.Product_Tag_3=Product_Tag_3
            pro.Product_Image=Product_Image
            pro.save()
            message = 'Product Updated Sucessfully'
            status = 'success'
        except Exception as err:
            print(err)
            message = 'Product Not Updated'
            status = 'warning'
        return render(request,'admin_dashboard/edit_product.html',{'act4':'active','message':message,'status':status,"prod":pro,"cat":cat})
    return render(request,'admin_dashboard/edit_product.html',{'act4':'active','obj':'none',"prod":pro,"cat":cat})



@login_required(login_url='/login/')
def payment(request):
    return render(request,'admin_dashboard/payment.html',{'act5':'active'})


@login_required(login_url='/login/')
def edit_image(request):
    user = request.user
    profile = CustomUser.objects.get(username=user)
    if request.POST:
        image = request.FILES.get('image')
        profile.profile_image = image
        profile.save()
        return render(request,'admin_dashboard/editimage.html',{'act':'active','profile':profile,'status':'primary','message':'Profile Image Saved Sucessfully'})
    return render(request,'admin_dashboard/editimage.html',{'act':'active','profile':profile,'obj':'none'})

@login_required(login_url='/login/')
def add_member(request):
    return render(request,'admin_dashboard/add_member.html',{'act2':'active'})

@login_required(login_url='/login/')
def delete_member(request):
    Id = request.GET.get('id')
    user = CustomUser.objects.get(id=Id)
    user.delete()
    return redirect('/admin_dashboard/Members_details/?del=True')

@login_required(login_url='/login/')
def hire(request):
    if request.POST:
        Id = request.POST.get('id')
        jb = Job_request.objects.get(id=Id)
        cu = CustomUser.objects.create(username=jb.Email,password=make_password('12345678@'),user_type='Trainer').save()
        cu = CustomUser.objects.get(username=jb.Email)
        td = Trainer_Details.objects.create(User=cu,Name=jb.Name,Email=jb.Email,Address=jb.Address,
            facebook=jb.facebook,twitter=jb.twitter,instagram=jb.instagram).save()
        jb.delete()
        url = '/admin_dashboard/job_request/?hire=True'
        return redirect(url)
    return redirect('/admin_dashboard/job_request/')