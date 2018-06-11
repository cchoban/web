from rest_framework import serializers
from .models import Package, SubmitPackage

class PackageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Package
        fields = '__all__'

class SubmitPackageSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubmitPackage
        fields = '__all__'

