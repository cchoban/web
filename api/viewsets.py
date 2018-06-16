from rest_framework import viewsets
from .models import Package, SubmitPackage
from .serializers import PackageSerializer, SubmitPackageSerializer
from . import helpers
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Package.objects.all()
    serializer_class = PackageSerializer


class SubmitPackageViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = SubmitPackage.objects.all()
    serializer_class = SubmitPackageSerializer
    http_method_names = ['get', "post"]
    lookup_field = "packageName"

    def create(self, request):
        package = self.request.data.get("package")

        packageExists = SubmitPackage.objects.filter(packageName=self.request.data.get("packageName").lower())[:1].exists()
        if not packageExists:
            if self.request.FILES["package"] and self.request.data.get("packageName"):
                uploaded = helpers.handle_uploaded_files(self.request.FILES['package'])
                if isinstance(uploaded, dict) and uploaded != False:
                    serializer = SubmitPackageSerializer(data=request.data)
                    validated = serializer.is_valid()
                    if validated:
                        serializer.save(packageName=uploaded["packageArgs"]["packageName"].lower(),
                                        packageArgs=uploaded["packageArgs"],
                                        packageUninstallArgs=uploaded["packageUninstallArgs"],
                                        server=uploaded["server"])

                        helpers.cleanup(self.request.data.get("packageName"))

                    return Response({"success": "You successfully submitted your package."}, status=status.HTTP_201_CREATED)
                else:
                    return Response({"error": "Could not push your package."}, status=status.HTTP_406_NOT_ACCEPTABLE)
        else:
            return Response({"error": "This package is already under approvement period."}, status=status.HTTP_406_NOT_ACCEPTABLE)
