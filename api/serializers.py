from rest_framework import serializers
from .models import Package, SubmitPackage
from django.contrib.auth import authenticate
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User

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

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        username = data.get("username", "")
        password = data.get("password", "")

        if username and password:
            user = authenticate(username=username, password=password)
            if user:
                if user.is_active:
                    data["user"] = user
                else:
                    msg = "User is deactivated."
                    raise ValidationError(msg)
            else:
                msg = "Unable to login with given credentials."
                raise ValidationError(msg)
        else:
            msg = "Must provide username and password both."
            raise ValidationError(msg)

        return data
