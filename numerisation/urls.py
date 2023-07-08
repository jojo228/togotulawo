from django.urls import path
from numerisation.views import *


urlpatterns = [
    #HomePage urls
    path('', home, name='home'),
    
]
