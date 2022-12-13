from rest_framework import serializers

from main.models.article import Article, Comment
from main.models.newsletter import Subscribers
from main.models.paiement import Payment
from main.models.user_article import UserArticle


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['title', 'slug', 'subtitle', 'contenu', 'couverture', 'auteur', 'domaine',
        'type', 'resource', 'video_link', 'discount', 'price', 'is_draft',
        'active', 'date_created', 'date_modified', 'publish_date',]


class UserArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserArticle
        fields = ['user', 'article', 'date',]


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['user', 'article', 'text', 'rate', 'date',]


class SubscribersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscribers
        fields = ['email', 'date',]


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ['order_id', 'paygate_payment_id', 'payment_reference', 'user_article', 'user', 
        'phone_number', 'network', 'article', 'date', 'status',]