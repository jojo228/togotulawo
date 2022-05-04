from django.urls import path
from dashboard.views import HomePage
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    #HomePage urls
    path('', HomePage, name='tableau'),


]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
