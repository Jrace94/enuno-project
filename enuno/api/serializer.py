from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth import authenticate
from .models import Corp


class CorpSerializer(serializers.ModelSerializer):
    class Meta:
        model = Corp
        fields = "__all__"


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def validate(cls, attrs):
        user = authenticate(username=attrs["username"], password=attrs["password"])
        if user is None or (
            attrs["username"] != "admin" or attrs["password"] != "admin"
        ):
            raise serializers.ValidationError("Invalid username or password")

        data = super().validate(attrs)
        return data
