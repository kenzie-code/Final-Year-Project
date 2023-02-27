from django.urls import path,include
from .views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('signup/',signup),
    path('login/',userLogin),
    path('logout/',userLogout),
    path('trainer_dashboard/',trainer_dashboard),
]

if settings.DEBUG:
    urlpatterns = urlpatterns+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
    urlpatterns = urlpatterns +static(settings.STATIC_URL,document_root=settings.STATICFILES_DIRS)