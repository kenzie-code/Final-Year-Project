from django.contrib import admin
from .models import *
from django.contrib.auth.models import User

# Register your models here.
admin.site.register(CustomUser)
admin.site.register(Customer_Details)
admin.site.register(Trainer_Details)
