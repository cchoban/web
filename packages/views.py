from django.shortcuts import render, redirect, get_object_or_404
import os
import json
from api import helpers as api_helpers
from . import helpers
from api.models import Package, Setting, Category
from django.conf import settings
from django.http import JsonResponse, HttpResponse, Http404
from django.urls import reverse
from .forms import LoginForm, RegisterForm
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required
from rest_framework.authtoken.models import Token
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django_gravatar.helpers import get_gravatar_url, has_gravatar, get_gravatar_profile_url, calculate_gravatar_hash
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.views import APIView


def index(request):

    email = request.user.email if request.user.is_authenticated else ""
    context = {
        "maxEntry": settings.REST_FRAMEWORK["PAGE_SIZE"],
        "userPicture": get_gravatar_url(email, size=650)
    }

    return render(request, "index.html", context)

def category_index(request, category_name):
    category = get_object_or_404(Category, slug=category_name)
    packages = Package.objects.filter(category=category)

    context = {
        "category": category,
        "packages": packages,
        "catname": category.name
    }
    return render(request, "category_page.html", context)


def popular_index(request):
    context = {
        'maxentry': settings.REST_FRAMEWORK["PAGE_SIZE"]
    }
    return render(request, 'popular_page.html', context)


def ListAllPackages(request):
    context = {
        'maxentry': settings.REST_FRAMEWORK["PAGE_SIZE"]
    }

    return render(request, 'packages_page.html', context)
def register_view(request):
    form = RegisterForm(request.POST or None)
    context = {
        "register_form": form,
        "message": "",
        "success": None,
        "error":None,
        "redirect": False
    }

    if request.method == "POST":
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password1")

            if request.user.is_authenticated:
                return redirect("/")

            try:
                createUser = form.save()

                auth = authenticate(username=username, password=password)
                login_to_system = login(request, auth)

                context["success"] = True
                context["message"] = "You have successfully registered."
                context["redirect"] = True
            except Exception as e:
                print(e)
                context["error"] = True
                context["message"] = "Could not register, please try again another time."

    print(context)
    return render(request, "auth/register.html", context)


def getPackage(request, packageName):

    id = Package.objects.filter(packageArgs__packageName=packageName)[:1]

    context = {
        "packageName": packageName,
        "packageId": id
    }
    return render(request, "single.html", context)

class LoginView(TemplateView):
    def get(self, request):
        context = {
            "form": LoginForm
        }
        return render(request, 'auth/login.html', context)

    def post(self, request):
        form = AuthenticationForm(None, request.POST)
        response_data = {}


        if request.user.is_authenticated:
            return self.__returnMessage(request, False, "You're already logged in!")

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            try_login = login(request, user)
            return self.__returnMessage(request, True, 'Successfully logged in, you\'ll be redirected soon')
        else:
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            if not username or not password:
                return self.__returnMessage(request, False, 'You have empty field(s). Please fill them if you want to contiune')

            errors = []
            for i in form.errors.get('__all__'):
                errors.append(i)

            errors = '\n'.join(errors)
            return self.__returnMessage(request, False, errors)

        if request.is_ajax():
            return self.__returnMessage(request, True, "tamam")
        else:
            response_data['form'] = form
            return render(request, 'auth/login.html', response_data)


    def __returnMessage(self, request, status, message):
        if request.is_ajax():
            return JsonResponse({
                "status": status,
                "message": message
            })
        else:
            context = {
                "message": message
            }
            if status:
                context["success"] = True
            else:
                context["error"] = True

            print(context)
            return render(request, 'auth/login.html', context)

class AccountView(TemplateView):
    '''
    Profile page for user
    '''
    def get(self, request, username = ""):
        context = {}
        user_details = get_object_or_404(User, username=username)
        user_packages = Package.objects.filter(user=user_details.id)

        if has_gravatar(user_details.email):
            context["profile_picture"] = get_gravatar_url(user_details.email, size=650)


        context["user_package_count"] = len(user_packages)
        context["username"] = user_details.username
        context["user_packages"] = user_packages
        return render(request, 'auth/account.html', context)

class AccountTokenView(LoginRequiredMixin, TemplateView):
    def get(self, request):
        context = {}
        return render(request, 'auth/get_token.html', context)

    def post(self, request):
        token = Token.objects.filter(user=request.user)
        if token.exists() and not request.POST.get('generate_new_token'):
            return JsonResponse({"status": False, "message": "Your account has already a token.", "key": token.get(user=request.user).key})
        elif request.POST.get('generate_new_token'):
            update_token = Token.objects.filter(user=request.user)
            update_token.delete()


        create_token = Token.objects.create(user=request.user)
        if create_token:
            return JsonResponse({"status": True, "message": "You successfully generated your new key!", "key": create_token.key})



@api_view(['GET'])
# @authentication_classes((TokenAuthentication,))
# @permission_classes((IsAuthenticated,))
def package_list(request):
    packages = Package.objects.all()
    do_update = Setting.objects.filter(do_update_packages=True)

    json = helpers.__check_for_cached_repo()

    if do_update and do_update[0].do_update_packages == True:
        json = {}
        for i in packages:
            json.update({
                i.packageName: settings.URL +
                "/api/packages/"+str(i.id)+"?format=json"
            })
        helpers.__write_cache(json)

    if isinstance(json, dict) and len(json) == 0:
        json = {}
        for i in packages:
            json.update({
                i.packageName: settings.URL +
                "/api/packages/"+str(i.id)+"?format=json"
            })

    return JsonResponse(json)

@require_http_methods(["GET"])
def is_logged(request):
    if request.user.is_authenticated:
        return JsonResponse({"auth": True})
    else:
        return JsonResponse({"auth": False})
