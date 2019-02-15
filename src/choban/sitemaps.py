from django.contrib.sitemaps import Sitemap
from api.models import Package
from django.conf import settings

class PackageSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.5

    def items(self):
        return Package.objects.all()

    def lastmod(self, obj):
        return obj.updated_at

    def location(self, item):
        return '/packages/'+str(item)
