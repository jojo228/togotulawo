from django.urls import path
from dashboard.views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    #HomePage urls
    path('', HomePage, name='tableau'),
    path('publier/' , publier, name="publier"),
    path('article-detail/<slug>', article_detail , name="article_detail"),
    path('liste-article/' , see_article , name="liste_article"),
    path('brouillon/' , Brouillon , name="brouillon"),

    path('profil/' , Profil , name="profil"),

    path('delete-article/<id>' , article_delete , name="article_delete"),
    path('update-article/<slug>/' , article_update , name="article_update"),


]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
