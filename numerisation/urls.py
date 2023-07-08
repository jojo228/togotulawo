from django.urls import path
from .views import *


urlpatterns = [
    #HomePage urls
    path('', home, name='home'),
    
]
