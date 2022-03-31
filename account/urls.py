
from django.contrib import admin
from django.urls import include, path
from django.shortcuts import HttpResponse
from account.views import LoginView, SignupView, signout
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [

    #Authentication urls
    path('login', LoginView.as_view() , name = 'login'),
    path('signup', SignupView.as_view() , name = 'signup'),
    path('logout', signout , name = 'logout'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
