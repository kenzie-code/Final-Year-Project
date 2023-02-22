from django.urls import path,include
from .views import *


urlpatterns = [
    path('',home),
    path('signup/',signup),
    path('login/',login),
    path('admin_dashboard/',admin_dashboard),
    path('customer_dashboard/',customer_dashboard),
    path('trainer_dashboard/',trainer_dashboard),
]
