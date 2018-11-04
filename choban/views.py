from django.shortcuts import render
from django.urls import reverse
from api.models import Package


def sitemap_index(request):
    sitemaps = {
        'Package': {
            'url': reverse('SitemapPackage'),
            'lastmod': Package.objects.filter().order_by('-updated_at')[0].updated_at
        }
    }
    context = {
        'sitemap_index': sitemaps
    }
    return render(request, 'sitemap_index.html', context)
