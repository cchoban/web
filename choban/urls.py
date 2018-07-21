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
from packages import urls as packageUrls
from packages.views import is_logged, register_view
from django.contrib.auth.views import logout, login
from packages.views import AccountTokenView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls), name="api"),
    path('packages', include(packageUrls)),
    path("login", login, {"template_name": "auth/login.html"}, name="LoginPage"),
    path("register", register_view, name="RegisterPage"),
    path('logout', logout, {'next_page': '/'}),
    path('account', logout, {'next_page': '/'}, name="AccountPage"),
    path('account/token', AccountTokenView.as_view(), name='TokenPage'),


    path("islogged", is_logged)
]
