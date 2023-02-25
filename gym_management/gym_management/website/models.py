from django.db import models

# Create your models here.
class Information(models.Model):
    maild_id = models.CharField(max_length=50,verbose_name="Business Mail",null=True,blank=True)
    phone_no = models.CharField(max_length=10,verbose_name="Phone No",null=True,blank=True)
    country_code = models.CharField(max_length=5,verbose_name="Country Code",null=True,blank=True)
    business_address = models.TextField(null=True,blank=True)

class social_info(models.Model):
    title = models.CharField(max_length=100,verbose_name="Platform",null=True,blank=True)
    icon_class = models.CharField(max_length=50,verbose_name="Icon Class",null=True,blank=True)
    url = models.URLField(null=True,blank=True)

class cards(models.Model):
    Name = models.CharField(max_length=100,verbose_name="Name",null=True,blank=True)
    Content = models.TextField(null=True,blank=True)


class headline_cards(models.Model):
    Name = models.CharField(max_length=100,verbose_name="Name",null=True,blank=True)
    short_description = models.CharField(max_length=250,verbose_name="Short Description",null=True,blank=True)
    Content = models.TextField(null=True,blank=True)

class Gallery(models.Model):
    Title = models.CharField(max_length=100,verbose_name="Title",null=True,blank=True)
    photos = models.ImageField(upload_to='media/',null=True,blank=True)


    