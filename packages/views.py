from django.shortcuts import render
import os
import json
from api import helpers as api_helpers
from . import helpers
from api.models import Package, Setting
from django.conf import settings
from django.http import JsonResponse
from django.urls import reverse
from rest_framework.authentication import TokenAuthentication

from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.views import APIView
# Create your views here.


def index(request):

    context = {
        "maxEntry": settings.REST_FRAMEWORK["PAGE_SIZE"]
    }

    return render(request, "index.html", context)


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
