from rest_framework import viewsets
from .models import Package, SubmitPackage
from .serializers import PackageSerializer, SubmitPackageSerializer
from . import helpers
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.exceptions import ValidationError, PermissionDenied

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Package.objects.all()
    serializer_class = PackageSerializer


class SubmitPackageViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    queryset = SubmitPackage.objects.all()
    serializer_class = SubmitPackageSerializer
    http_method_names = ['get', "post"]

    def perform_create(self, serializer):
        package = self.request.data.get("package")
        packageName = str(package).split(".")[0]

        try:
            packageExists = get_object_or_404(SubmitPackage, packageName=packageName)
            print(packageExists)
            if packageExists:
                return Response(404)
        except Exception as e:
            return False



        if self.request.FILES["package"]:
            print("sa")
            uploaded = helpers.handle_uploaded_files(self.request.FILES['package'])

            if isinstance(uploaded, dict) and uploaded != False:
                serializer.save(
                    package=str(package),
                    packageName=uploaded["packageArgs"]["packageName"],
                    packageArgs=uploaded["packageArgs"],
                    packageUninstallArgs=uploaded["packageUninstallArgs"],
                    server=uploaded["server"]
                )

                helpers.cleanup(packageName)
            else:
                return Response("Could not push your package.")
