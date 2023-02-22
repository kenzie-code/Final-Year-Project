from django.db.models.signals import pre_save,post_save
from django.dispatch import receiver
from .models import *

@receiver(post_save,sender=CustomUser)
def createprofile(sender,instance,created,**kwargs):
    print('Run')
    if created:
        if instance.user_type == "Customer":
            data = Customer_Details.objects.create(User=instance)
            data.save()
        else :
            data = Trainer_Details.objects.create(User=instance)
            data.save()
    else :
        pass
