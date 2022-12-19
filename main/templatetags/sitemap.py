from django.contrib.sitemaps import Sitemap
from main.models.article import Article


class ArticleSiteMap(Sitemap):

    priority = 1.0
    changefreq = 'daily'

    def items(self):
        return Article.objects.all()

    def location(self, item):
        return "/article/" + str(item) 