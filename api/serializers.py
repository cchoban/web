from rest_framework import serializers
from .models import Package, SubmitPackage


class PackageSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category')
    user_name = serializers.CharField(source='user')
    class Meta:
        model = Package
        fields = '__all__'


class SubmitPackageSerializer(serializers.ModelSerializer):

    class Meta:
        model = SubmitPackage
        fields = '__all__'
