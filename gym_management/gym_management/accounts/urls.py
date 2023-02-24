from django.urls import path,include
from .views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('',home),
    path('signup/',signup),
    path('login/',login),
    path('admin_dashboard/',admin_dashboard),
    path('customer_dashboard/',customer_dashboard),
    path('trainer_dashboard/',trainer_dashboard),
]
urlpatterns = urlpatterns +static(settings.STATIC_URL,document_root=settings.STATICFILES_DIRS)
