"""gym URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from website.views import *
from . import views
urlpatterns = [
    path('',home),
    path('about_us/', about),
    path('pricing/', pricing),
    path('concept/', concept) ,
    path('contact/', contact) ,
    path('review/',review),
    path('job_request/',job_req),
    path('gold_member/', gold_member),
    path('first_timer/', first_timer),
    path('personal_training/', personal_training),
    path('holy_booty/', holy_booty),
    path('holy_box/', holy_box),
    path('holy_ride/', holy_ride),
    path('holy_shred/', holy_shred),
    path('Perso/', views.Perso),
    
    
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
urlpatterns = urlpatterns +static(settings.STATIC_URL,document_root=settings.STATICFILES_DIRS)