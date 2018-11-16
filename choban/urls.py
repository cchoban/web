"""choban URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from .routers import router
from django.contrib.sitemaps.views import sitemap
from . import sitemaps
from .views import sitemap_index as index
from api.views import GetPackages
from django.conf import settings
from django.conf.urls.static import static
sitemap_index = {
    'Package': sitemaps.PackageSitemap,
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls), name="api"),
    path('api/repo/', GetPackages.as_view(), name="PackageRepo"),
    path('sitemap_index.xml', index, name='Sitemap'),
    path('sitemap_package.xml', sitemap, {'sitemaps': sitemap_index, 'template_name': 'package-sitemap.html'},
         name='SitemapPackage'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
