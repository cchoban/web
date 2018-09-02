from django.urls import path
from packages.views import register_view, logout_view, AccountView, AccountTokenView
from .views import LoginView

urlpatterns = [
    path("login", LoginView.as_view(), name="LoginPage"),
    path("register", register_view, name="RegisterPage"),
    path('logout', logout_view, name="LogoutPage"),
    path('user/<slug:username>', AccountView.as_view(), name="AccountPage"),
    path('token', AccountTokenView.as_view(), name='TokenPage'),

]
