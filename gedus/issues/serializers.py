from rest_framework import serializers

from entreprise.models import Postuler, Issues


class IssuesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Issues
        fields = ['entreprise', 'titre', 'domaine', 'description', 'slug', 
        'profil_rechercher', 'duree_recherche', 'is_draft', 'active', 'publish_date',]


class PostulerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Postuler
        fields = ['issues', 'nom_du_candidat', 'prenom_du_candidat', 'contact_du_candidat', 
        'email_du_candidat', 'motivation_du_candidat', 'postule_date',]