from django.db import models
# Create your models here.
class Type(models.Model):
    Name = models.CharField(unique=True,max_length=100,verbose_name='Package Type')

    def __str__(self):
        return self.Name

class Package(models.Model):
    Name = models.CharField(unique=True,max_length=100,verbose_name='Package')
    Price = models.IntegerField()
    Type = models.ForeignKey(Type,null=True,blank=True,on_delete=models.SET_NULL)
    Description = models.TextField()

    def __str__(self):
        return self.Name





