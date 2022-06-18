from django.urls import path
from entreprise.views import home_page, problematique_create, problematique_delete, problematique_list, problematique_read, problematique_update, entreprise_profil, problematique_draft, postule_list
from django.conf import settings
from django.conf.urls.static import static

app_name = 'entreprise'


urlpatterns = [
    # HomePage urls
    path('', home_page, name='home'),

    #Problématique
    path('publier/', problematique_create, name="prob_create"),
    path('prob-detail/<slug>', problematique_read, name="prob_detail"),
    path('prob-list/', problematique_list, name="prob_list"),
    path('prob-draft/', problematique_draft, name="prob_draft"),
    path('prob-delete/<id>', problematique_delete, name="prob_delete"),
    path('prob-update/<slug>/', problematique_update, name="prob_update"),

    path('profil/', entreprise_profil, name="ense_profil"),

    #Postuler
    path('postule_list/', postule_list, name="postule_list"),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
