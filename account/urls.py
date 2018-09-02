from django.urls import path
from .views import LoginView, RegisterView, logout_view, AccountView, AccountTokenView

urlpatterns = [
    path("login", LoginView.as_view(), name="LoginPage"),
    path("register", RegisterView.as_view(), name="RegisterPage"),
    path('logout', logout_view, name="LogoutPage"),
    path('user/<slug:username>', AccountView.as_view(), name="AccountPage"),
    path('token', AccountTokenView.as_view(), name='TokenPage'),

]
