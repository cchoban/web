from django.shortcuts import render, redirect
import os
import json
from api import helpers as api_helpers
from . import helpers
from api.models import Package, Setting
from django.conf import settings
from django.http import JsonResponse, HttpResponse, Http404
from django.urls import reverse
from .forms import LoginForm, RegisterForm
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.http import require_http_methods
from rest_framework.authtoken.models import Token
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.views import APIView


def index(request):

    context = {
        "maxEntry": settings.REST_FRAMEWORK["PAGE_SIZE"]
    }

    return render(request, "index.html", context)


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