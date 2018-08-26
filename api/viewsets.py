from rest_framework import viewsets, filters
from .models import Package, SubmitPackage, Setting
from .serializers import PackageSerializer, SubmitPackageSerializer
from . import helpers
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Package.objects.all()
    serializer_class = PackageSerializer
    filter_backends = (filters.SearchFilter,
                       filters.OrderingFilter, DjangoFilterBackend, )
    filter_fields = ['category']
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
    http_method_names = ['get', "post"]
    lookup_field = "packageName"

    def create(self, request):
        package = self.request.data.get("package")
        package_name = self.request.data.get("packageName")

        if package_name != str(package).split(".")[0]:
            return Response({"error": "Could not accept your request."}, status=status.HTTP_406_NOT_ACCEPTABLE)

        packageExists = Package.objects.filter(
            packageName=package_name.lower())[:1].exists()
        packageOwner = Package.objects.filter(
            packageName=package_name.lower(), user=self.request.user.id).exists()

        submitPackages_packageOwner = SubmitPackage.objects.filter(
            packageName=package_name.lower(), user=self.request.user.id).exists()

        submitPackageExists = SubmitPackage.objects.filter(
            packageName=package_name.lower())[:1].exists()

        # if packageExists and not packageOwner and not submitPackages_packageOwner:
        #     return Response({"error": "This package is already published."}, status=status.HTTP_406_NOT_ACCEPTABLE)

        if not submitPackageExists:
            if self.request.FILES["package"] and self.request.data.get("packageName"):
                uploaded = helpers.handle_uploaded_files(
                    self.request.FILES['package'])

                if not bool(uploaded["status"]):
                    return Response({"error": uploaded["message"]}, status=status.HTTP_406_NOT_ACCEPTABLE)

                if isinstance(uploaded, dict) or uploaded != False:
                    serializer = SubmitPackageSerializer(data=request.data)
                    validated = serializer.is_valid()
                    if validated:
                        serializer.save(packageName=uploaded["packageArgs"]["packageName"].lower(),
                                        packageArgs=uploaded["packageArgs"],
                                        packageUninstallArgs=uploaded[
                                            "packageUninstallArgs"],
                                        server=uploaded["server"],
                                        user=request.user
                                        )
                        Setting.objects.update(do_update_packages=True)
                        helpers.cleanup(self.request.data.get("packageName"))

                    return Response({"success": "You successfully submitted your package."}, status=status.HTTP_201_CREATED)
                else:
                    return Response({"error": "Could not push your package."}, status=status.HTTP_406_NOT_ACCEPTABLE)
        else:
            return Response({"error": "This package is already under approvement period."}, status=status.HTTP_406_NOT_ACCEPTABLE)
