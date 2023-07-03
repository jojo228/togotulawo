from django.urls import path
from entreprise.views import (
    app_print,
    doc_create,
    doc_delete,
    doc_list,
    doc_read,
    doc_update,
    home_page,
    postule_read,
    premium_request,
    problematique_create,
    problematique_delete,
    problematique_list,
    problematique_read,
    problematique_update,
    entreprise_profil,
    problematique_draft,
    postule_list,
)
from django.conf import settings
from django.conf.urls.static import static

#app_name = "entreprise"


urlpatterns = [
    # HomePage urls
    path("", home_page, name="home"),
    path("premium_request/", premium_request, name="premium_request"),
    path("app_print/<int:id>", app_print, name="app_print"),
    # Problématique
    path("publier/", problematique_create, name="prob_create"),
    path("prob-detail/<slug>", problematique_read, name="prob_detail"),
    path("prob-list/", problematique_list, name="prob_list"),
    path("prob-draft/", problematique_draft, name="prob_draft"),
    path("prob-delete/<id>", problematique_delete, name="prob_delete"),
    path("prob-update/<slug>/", problematique_update, name="prob_update"),
    # Livres
    path("ajouter/", doc_create, name="doc_create"),
    path("doc-detail/<str:slug>", doc_read, name="doc_detail"),
    path("doc-list/", doc_list, name="doc_list"),
    path("doc-delete/<id>", doc_delete, name="doc_delete"),
    path("doc-update/<id>/", doc_update, name="doc_update"),
    path("profil/", entreprise_profil, name="ense_profil"),
    # Postuler
    path("postule_list/", postule_list, name="postule_list"),
    path("postule_read/<int:id>", postule_read, name="postule_read"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
