from django.conf import settings
from django.urls import path
from django.conf.urls.static import static

from .views import *


urlpatterns = [
    #HomePage urls
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)