
from django.contrib import admin
from django.urls import path
from gedus.views import coming_soon
from django.conf import settings
from django.conf.urls.static import static


app_name = 'main'

urlpatterns = [
    path('', coming_soon, name='coming_soon'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
