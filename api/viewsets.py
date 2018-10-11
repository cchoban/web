from rest_framework import viewsets, filters
from .models import Package, SubmitPackage, Setting
from .serializers import PackageSerializer, SubmitPackageSerializer
from . import helpers
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from . import Logger as log

class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Package.objects.all()
    serializer_class = PackageSerializer
    filter_backends = (filters.SearchFilter,
                       filters.OrderingFilter, DjangoFilterBackend, )
    filter_fields = ['category', 'showcase']
    ordering_fields = ('created_at', 'updated_at', 'download_count', )
    search_fields = ("packageName",)
    http_method_names = ['get']

    def retrieve(self, request, pk=None):
        downloading = self.request.query_params.get('download')
        package = get_object_or_404(Package, pk=pk)
        serializer = PackageSerializer(package)

        if downloading == 'true':
            if not self.request.session.get('downloaded'):
                self.request.session['downloaded'] = True
                package.download_count += 1
                package.save()
        else:
            if not self.request.session.get('counted'):
                self.request.session['counted'] = True
                package.view_count += 1
                package.save()

        return Response(serializer.data)


class SubmitPackageViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = SubmitPackage.objects.all()
    serializer_class = SubmitPackageSerializer
    http_method_names = ['post']
    lookup_field = "packageName"

    def create(self, request):
        dump = helpers.dump_json
        package_name = self.request.data.get("packageName")
        package_args = dump(self.request.data.get('packageArgs'))
        package_uninstall_args = dump(self.request.data.get('packageUninstallArgs'))
        package_server=dump(self.request.data.get('server'))
        package_icon = self.request.data.get('packageIcon')

        validate = helpers.validate_json

        # print(package_name, package_args, package_uninstall_args, package_server, package_icon)
        if not package_name or not package_args or not package_uninstall_args or not package_server or not package_icon:
            return Response({'error': 'Please provide a package.'}, status=status.HTTP_406_NOT_ACCEPTABLE)

        # if not validate(package_args) or not validate(package_uninstall_args) or not validate(package_server):
        #     return Response({'error': 'Make sure you have created package with Choban.'}, status=status.HTTP_406_NOT_ACCEPTABLE)


        packageExists = Package.objects.filter(
            packageName=package_name.lower())[:1].exists()

        packageOwner = Package.objects.filter(
            packageName=package_name.lower(), user=self.request.user.id).exists()

        submitPackages_packageOwner = SubmitPackage.objects.filter(
            packageName=package_name.lower(), user=self.request.user.id).exists()

        submitPackageExists = SubmitPackage.objects.filter(
            packageName=package_name.lower())[:1].exists()

        if not submitPackageExists:
            check_version = helpers.check_package_version(package_args)

            if not bool(check_version['status']):
                return Response({'error': check_version['message']}, status=status.HTTP_406_NOT_ACCEPTABLE)
            try:
                serializer = SubmitPackageSerializer(data=request.data)
                validated = serializer.is_valid()
                if validated:
                    create = serializer.save(packageName=package_name,
                                            packageArgs=package_args,
                                            packageUninstallArgs=package_uninstall_args,
                                            server=package_server,
                                            packageIcon=package_icon,
                                            user=request.user
                    )

                    update = Setting.objects.update(do_update_packages=True)

                    if create and update:
                        return Response({"success": "You successfully submitted your package."}, status=status.HTTP_201_CREATED)
                    else:
                        return Response({"success": "Could not accept your package, please try again later."}, status=status.HTTP_406_NOT_ACCEPTABLE)
                else:
                    return Response({'error': 'Your files could not be validated.'}, status=status.HTTP_406_NOT_ACCEPTABLE)
            except Exception as e:
                return Response({'error': str(e)})
                log.new(e).logError()
                return False
        else:
            return Response({"error": "This package is already under approvement period."}, status=status.HTTP_406_NOT_ACCEPTABLE)
