from django.db import models
from accounts.models import CustomUser
from appadmin.models import Package
# Create your models here.
class Feedback(models.Model):
    User = models.ForeignKey(CustomUser,on_delete=models.CASCADE,related_name='Feedback')
    subject = models.CharField(max_length=100,verbose_name="Subject")
    content = models.TextField()

class Bill(models.Model):
    User = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    payment_date = models.DateField(auto_now_add=True)
    amount = models.FloatField()
    method = models.CharField(max_length=100)
    transaction_id = models.SlugField(auto_created=True)

class Membership(models.Model):
    User = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    Package_Details = models.ForeignKey(Package,null=True,on_delete=models.SET_NULL)
    start_date = models.DateField(auto_now_add=True)
    end_date = models.DateField(null=False)
    Bill = models.OneToOneField(Bill,null=True,on_delete=models.SET_NULL)



