from django.contrib.sitemaps import Sitemap
from gedus.main.models import Article


class ArticleSiteMap(Sitemap):
    priority = 1.0
    changefreq = "daily"

    def items(self):
        return Article.objects.all()

    def location(self, item):
        return "/gedus/article/" + str(item)
