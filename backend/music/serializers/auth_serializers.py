from ..models import Auth
from rest_framework import serializers     
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.settings import api_settings
from django.contrib.auth.models import update_last_login
from django.core.exceptions import ObjectDoesNotExist

class AuthSerializer(serializers.ModelSerializer):

    class Meta:
        model = Auth
        fields = ['id', 'username', 'email', 'is_active', 'is_superuser', 'created', 'updated']
        read_only_field = ['is_active', 'created', 'updated', 'is_superuser']
        



class LoginSerializer(TokenObtainPairSerializer):

     def validate(self, attrs):
        data = super().validate(attrs)

        refresh = self.get_token(self.user)

        data['user'] = AuthSerializer(self.user).data
        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)

        if api_settings.UPDATE_LAST_LOGIN:
            update_last_login(None, self.user)

        return data


class RegisterSerializer(AuthSerializer):
    password = serializers.CharField(max_length=128, min_length=8, write_only=True, required=True)
    email = serializers.EmailField(required=True, write_only=True, max_length=128)

    class Meta:
        model = Auth
        fields = ['id', 'username', 'email', 'password', 'is_active', 'created', 'updated']

    def create(self, validated_data):
        try:
            user = Auth.objects.get(email=validated_data['email'])
        except ObjectDoesNotExist:
            user = Auth.objects.create_user(**validated_data)
        return user