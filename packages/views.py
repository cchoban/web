from django.shortcuts import render, redirect
import os
import json
from api import helpers as api_helpers
from . import helpers
from api.models import Package, Setting
from django.conf import settings
from django.http import JsonResponse, HttpResponse, Http404
from django.urls import reverse
from rest_framework.authentication import TokenAuthentication

from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.views import APIView
from .forms import LoginForm, RegisterForm
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.http import require_http_methods
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