from django.urls import path
from dashboard.views import home_page, article_create, article_delete, article_list, article_read, article_update, author_profil, article_draft, sale
from django.conf import settings
from django.conf.urls.static import static

app_name = 'dashboard'

urlpatterns = [
    #HomePage urls
    path('', home_page, name='tableau'),
    path('publier/' , article_create, name="publier"),
    path('article-detail/<slug>', article_read , name="article_detail"),
    path('liste-article/' , article_list , name="liste_article"),
    path('brouillon/' , article_draft , name="brouillon"),
    path('delete-article/<id>' , article_delete , name="article_delete"),
    path('update-article/<slug>/' , article_update , name="article_update"),

    path('profil/' , author_profil , name="profil"),
    path('ventes/' , sale , name="ventes"),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
