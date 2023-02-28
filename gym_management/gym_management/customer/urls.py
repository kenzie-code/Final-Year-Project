from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_dash),
    path('Membership_details/',views.Membership_details),
    path('reviews/',views.Reviews),
    path('Products/',views.Products_sec),
    path('cart/',views.yourcart),
    path('edit_profile/', views.edit_profile),
    path('edit_password/', views.edit_password),
    path('edit_image/', views.edit_image),
]