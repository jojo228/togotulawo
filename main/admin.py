from django.contrib import admin
from main.models.article import Article, Categorie, Comment, CouponCode, Tag, TypeDoc
from main.models.paiement import Payment
from main.models.user_article import UserArticle
from main.models.video import Video
from django.utils.html import format_html
# Register your models here.


class TagAdmin(admin.TabularInline):
    model = Tag


class TypeDocAdmin(admin.TabularInline):
    model = TypeDoc


class VideoAdmin(admin.TabularInline):
    model = Video



class CategorieAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}



class ArticleAdmin(admin.ModelAdmin):
    inlines = [TagAdmin,  VideoAdmin]
    list_display = ["title", 'get_price', 'get_discount', 'active']
    list_filter = ("discount", 'active')
    prepopulated_fields = {"slug": ("title",)}

    def get_discount(self, article):
        return f'{article.discount} %'

    def get_price(self, article):
        return f'{article.price} f cfa'

    get_discount.short_description = "Discount"
    get_price.short_description = "Price"


class PaymentAdmin(admin.ModelAdmin):
    model = Payment
    list_display = ["order_id", 'get_user', 'get_article', 'status']
    list_filter = ["status", 'article']

    def get_user(self, payment):
        return format_html(f"<a target='_blank' href='/admin/auth/user/{payment.user.id}'>{payment.user}</a>")

    def get_article(self, payment):
        return format_html(f"<a target='_blank' href='/admin/articles/article/{payment.article.id}'>{payment.article}</a>")

    get_article.short_description = "Article"
    get_user.short_description = "User"


class UserArticleAdminModel(admin.ModelAdmin):
    model = UserArticle
    list_display = ['click', 'get_user', 'get_article']
    list_filter = ['article']

    def get_user(self, userarticle):
        return format_html(f"<a target='_blank' href='/admin/auth/user/{userarticle.user.id}'>{userarticle.user}</a>")

    def click(self, userarticle):
        return "Click to Open"

    def get_article(self, userarticle):
        return format_html(f"<a target='_blank' href='/admin/articles/article/{userarticle.article.id}'>{userarticle.article}</a>")

    get_article.short_description = "Article"
    get_user.short_description = "User"


admin.site.register(Article, ArticleAdmin)
admin.site.register(Video)
admin.site.register(Payment, PaymentAdmin)
admin.site.register(UserArticle, UserArticleAdminModel)
admin.site.register(CouponCode)
admin.site.register(Categorie, CategorieAdmin)
admin.site.register(TypeDoc)
admin.site.register(Comment)
