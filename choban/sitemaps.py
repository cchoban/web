from django.contrib.sitemaps import Sitemap
from api.models import Package


class PackageSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.5

    def items(self):
        return Package.objects.all()

    def lastmod(self, obj):
        return obj.updated_at
