from django.shortcuts import render
from api.models import Package
from django.conf import settings

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
