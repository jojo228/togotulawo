from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns

from rest_framework import routers
from account import views

from django.conf import settings
from django.conf.urls.static import static

from django.contrib.sitemaps.views import sitemap

from main.templatetags.sitemap import ArticleSiteMap


router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)


sitemaps = {
    'article': ArticleSiteMap(),
}


urlpatterns = [
    path('', include("landing.urls")),
    path('gedus/', include("gedus.urls")),
    path('account/', include('account.urls', namespace='account')),
    path('dashboard/', include('dashboard.urls')),
    path('entreprise/', include('entreprise.urls')),
    path('tdm/', include('tdm.urls')),
    path('numerisation/', include('numerisation.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path("i18n/", include("django.conf.urls.i18n")),
    #REST-API urls
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('', include(router.urls)),
    #path('sitemap.xml', sitemap, {'sitemaps':sitemaps}, name='django.contrib.sitemaps.views.sitemap')
    path("ckeditor/", include("ckeditor_uploader.urls", namespace='ckeditor_uploader')),
]

urlpatterns += i18n_patterns(path("admin/", admin.site.urls))

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
