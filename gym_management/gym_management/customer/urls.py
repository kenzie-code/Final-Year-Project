from django.urls import path
from . import views

urlpatterns = [
    path('customer_dashboard/', views.home_dash),
    path('customer_dashboard/Membership_details/',views.Membership_details),
    path('customer_dashboard/reviews/',views.Reviews),
    path('customer_dashboard/Products/',views.Products_sec),
    path('customer_dashboard/cart/',views.yourcart),
    path('customer_dashboard/edit_profile/', views.edit_profile),
    path('customer_dashboard/edit_password/', views.edit_password),
]