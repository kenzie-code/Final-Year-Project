from django.db import models
# Create your models here.
class Type(models.Model):
    Name = models.CharField(unique=True,max_length=100,verbose_name='Package Type')

    def __str__(self):
        return self.Name

class Package(models.Model):
    Name = models.CharField(unique=True,max_length=100,verbose_name='Membership Package')
    Price = models.FloatField(null=True,blank=True)
    Type = models.ForeignKey(Type,null=True,blank=True,on_delete=models.SET_NULL)
    Description = models.TextField(null=True,blank=True)
    Duration = models.IntegerField(null=True,blank=True)
    Message = models.CharField(max_length=250,null=True,blank=True,verbose_name='Commitment Message')

    def __str__(self):
        return self.Name





