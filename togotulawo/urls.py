from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns

from django.conf import settings
from django.conf.urls.static import static

from django.contrib.sitemaps.views import sitemap

from gedus.templatetags.sitemap import ArticleSiteMap



sitemaps = {
    'article': ArticleSiteMap(),
}


urlpatterns = [
    path('', include("landing.urls")),
    path('gedus/', include("gedus.main.urls", "gedus.dashboard.urls", )),
    path('gedus/authentication/', include("gedus.authentication.urls")),
    path('tdm/', include('tdm.urls')),
    path('numerisation/', include('numerisation.urls')),
    path("i18n/", include("django.conf.urls.i18n")),
    #REST-API urls
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    #path('sitemap.xml', sitemap, {'sitemaps':sitemaps}, name='django.contrib.sitemaps.views.sitemap')
    path("ckeditor/", include("ckeditor_uploader.urls")),
]

urlpatterns += i18n_patterns(path("admin/", admin.site.urls))

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
