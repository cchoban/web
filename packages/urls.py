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
from django.urls import path
from .views import index, getPackage, package_list, is_logged, category_index, popular_index, ListAllPackages
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('/', index, name="PackagesPage"),
    path('/all', ListAllPackages, name="AllPackages"),
    path('/popular', popular_index, name="PopularPackages"),
    path('/category/<slug:category_name>',  category_index, name="CategoryPage"),
    path("/repo", package_list),
    path('/<slug:packageName>', getPackage, name="getPackage")
]
