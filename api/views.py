from rest_framework.views import APIView
from rest_framework.response import Response
from . import helpers
from .models import Package, Setting
from django.conf import settings


class GetPackages(APIView):

    def get(self, request):
        packages = Package.objects.all()
        do_update = Setting.objects.filter(do_update_packages=True)

        json = helpers.check_for_cached_repo()

        if do_update and do_update[0].do_update_packages == True:
            json = {}
            for i in packages:
                json.update({
                    i.packageName: settings.URL +
                                   "/api/packages/" + str(i.id) + "?format=json"
                })
            helpers.write_cache(json)

        if isinstance(json, dict) and len(json) == 0:
            json = {}
            for i in packages:
                json.update({
                    i.packageName: settings.URL +
                                   "/api/packages/" + str(i.id) + "?format=json"
                })

        return Response(json)
