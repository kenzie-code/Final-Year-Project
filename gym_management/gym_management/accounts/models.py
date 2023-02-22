from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin
import datetime
from .manager import *
from appadmin.models import Package

class CustomUser(AbstractBaseUser):
    User_Choices = (
        ("Trainer","Trainer"),
        ("Admin","Admin"),
        ("Customer","Customer")
    )
    id = models.AutoField(primary_key=True,unique=True)
    username = models.CharField(unique=True,max_length=50, verbose_name="Username")
    date_joined = models.DateTimeField(default=datetime.datetime.now)
    user_type = models.CharField(max_length = 20,choices = User_Choices,default = "Customer", verbose_name="User Type")
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ['user_type']
    objects = CustomUserManager()
    def __str__(self):
        return self.username
    def has_perm(self, perm, obj=None):
        return self.is_superuser

    def has_module_perms(self, app_label):
        return self.is_superuser

    def PostSave(sender,instance,**kwargs):
        print("Working")


class Customer_Details(models.Model):
    User = models.ForeignKey(CustomUser,on_delete=models.CASCADE,related_name='Customer_Details')
    Name = models.CharField(max_length=100,verbose_name="Name",null=False)
    Age = models.IntegerField(null=True,verbose_name="Age")
    Email = models.CharField(max_length=50,null=True,blank=True,verbose_name="Email")
    Address = models.TextField()
    Package = models.ForeignKey(Package,null=True,blank=True,on_delete=models.SET_NULL)
    Trainer = models.ForeignKey(CustomUser,null=True,blank=True,on_delete=models.SET_NULL)
    def __str__(self):
        return self.Name

class Trainer_Details(models.Model):
    User = models.ForeignKey(CustomUser,on_delete=models.CASCADE,related_name='Trainer_Details')
    Name = models.CharField(max_length=100,verbose_name="Name",null=False)
    Age = models.IntegerField(null=True,verbose_name="Age")
    Email = models.CharField(max_length=50,null=True,blank=True,verbose_name="Email")
    Address = models.TextField()
    Experience = models.IntegerField(null=True,verbose_name="Experience")
    Salary = models.FloatField(null=True,blank=True)
    Customer = models.ManyToManyField(Customer_Details,blank=True,related_name='Customer')
    def __str__(self):
        return self.Name

