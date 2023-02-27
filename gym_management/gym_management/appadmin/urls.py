from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_dash),
    path('trainer_details/',views.trainer_details),
    path('trainer_details/edit/',views.edit_trainer),
    path('trainer_details/add_trainer/',views.add_trainer),
    path('job_request/',views.job_request),
    path('Members_details/',views.Members_details),
    path('Members_details/edit/',views.edit_member),
    path('Reviews/',views.Reviews),
    path('Products/',views.Products_sec),
    path('Products/add/',views.add_product),
    path('payment/',views.payment),
    path('edit_password/',views.editpassword),
]