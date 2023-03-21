from django.db import models
# Create your models here.
class Type(models.Model):
    Name = models.CharField(unique=True,max_length=100,verbose_name='Package Type')

    def __str__(self):
        return self.Name

class Package(models.Model):
    themes_choice = (('Black','Black'),('white','White'))
    Name = models.CharField(unique=True,max_length=100,verbose_name='Membership Package')
    Price = models.FloatField(null=True,blank=True)
    Type = models.ForeignKey(Type,null=True,blank=True,on_delete=models.SET_NULL)
    Description = models.TextField(null=True,blank=True)
    Duration = models.IntegerField(null=True,blank=True)
    Message = models.CharField(max_length=250,null=True,blank=True,verbose_name='Commitment Message')
    theme = models.CharField(max_length=20,choices=themes_choice,blank=False,null=True)
    def __str__(self):
        return self.Name

class Job_request(models.Model):
    Name = models.CharField(max_length=200,null=False,blank=False,verbose_name="Name")
    profile_pic = models.ImageField(upload_to='media/job_request/profilepic/',null=True,blank=True)
    Email = models.EmailField(null=False,blank=False,verbose_name="Email")
    Phone = models.CharField(max_length=10,null=False,blank=False,verbose_name="Phone")
    Address = models.TextField(verbose_name='Address')
    Recent = models.CharField(max_length=500,verbose_name='Recent Experience')
    Past = models.CharField(max_length=500,verbose_name='Past Experience')
    facebook = models.URLField(null=True,blank=True,verbose_name='facebook')
    start_date = models.DateField(null=True,blank=True)
    twitter = models.URLField(null=True,blank=True,verbose_name='twitter')
    instagram = models.URLField(null=True,blank=True,verbose_name='instagram')
    cv = models.FileField(upload_to='media/job_request/cv/',null=False,blank=False,verbose_name='CV')


class Category(models.Model):
    Category_Name = models.CharField(max_length=200,unique=True,verbose_name='Category Name')


class Product(models.Model):
    Product_id = models.CharField(max_length=100,unique=True,verbose_name='Product Id')
    Product_Name = models.CharField(max_length=100,verbose_name='Product Name')
    Quantity = models.IntegerField(verbose_name='Quantity')
    Price = models.FloatField(verbose_name='Price',null=True,blank=True)
    Droping_Price = models.FloatField(verbose_name='Droping Price')
    Product_Description = models.TextField(verbose_name='Product Description',null=True,blank=True)
    Product_Category = models.ForeignKey(Category,on_delete=models.CASCADE,null=True,blank=True,verbose_name='Product Category')
    Product_Tag_1 = models.CharField(max_length=50,verbose_name='First Product Tag')
    Product_Tag_2 = models.CharField(max_length=50,verbose_name='Second Product Tag')
    Product_Tag_3 = models.CharField(max_length=50,verbose_name='Third Product Tag')
    Product_Image = models.ImageField(upload_to='media/product/',null=True,blank=True)
    Avg_Review = models.IntegerField(verbose_name='Average Review',default=0)
    
