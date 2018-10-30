from django.shortcuts import render, redirect, get_object_or_404
from . import helpers
from api.models import Package, Setting, Category
from django.conf import settings
from django.http import JsonResponse, HttpResponse, Http404
from django.views.decorators.http import require_http_methods
from django_gravatar.helpers import get_gravatar_url, has_gravatar, get_gravatar_profile_url, calculate_gravatar_hash
from rest_framework.decorators import api_view, authentication_classes, permission_classes


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


from rest_framework.response import Response
@api_view(['GET'])
def category_id(request, category_name):
    category = get_object_or_404(Category, slug=category_name)

    context = {
        "status": True,
        "category": category.id,
        "catname": category.name
    }
    return Response(context)



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


def EditorPicks(request):
    context = {
        'maxentry': settings.REST_FRAMEWORK['PAGE_SIZE']
    }

    return render(request, 'editor_picks.html', context)


def getPackage(request, packageName):

    id = Package.objects.filter(packageArgs__packageName=packageName)[:1]

    context = {
        "packageName": packageName,
        "packageId": id
    }
    return render(request, "single.html", context)


@api_view(['GET'])
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
