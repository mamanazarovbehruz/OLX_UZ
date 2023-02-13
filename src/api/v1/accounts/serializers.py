from rest_framework import serializers, exceptions
from rest_framework.authtoken.models import Token

from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate

from .models import CustomUser


class StaffRegisterSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ['phone_number', 'email', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def validate(self, attrs):
        if attrs['phone_number']:
            phone = CustomUser.objects.filter(phone_number=attrs['phone_number'])
            if phone:
                raise serializers.ValidationError(
                {'error': 'Your Phonenumber must be unique'})
        return attrs
    

class ClientRegisterSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ['phone_number', 'email', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }


    def validate(self, attrs):
        if attrs['phone_number']:
            phone = CustomUser.objects.filter(phone_number=attrs['phone_number'])
            if phone:
                raise serializers.ValidationError(
                {'error': 'Your Phonenumber must be unique'})
        return attrs


class UserSerializer(serializers.ModelSerializer):
    date_joined = serializers.DateTimeField(format='%Y-%m-%d %H:%M', read_only=True)
    class Meta:
        model = CustomUser
        exclude = ['id', 'is_active', 'is_deleted', 'is_staff', 'password',
                   'last_login', 'is_superuser', 'groups', 'user_permissions'
        ]
        read_only_fields = ['number_id', 'balance']


class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(source='email', max_length=128)
    password = serializers.CharField(max_length=128, write_only=True)


    def validate(self, data):
        username = data.get('email')
        password = data.get('password')
        user = get_object_or_404(CustomUser, email=username)
        if not user.check_password(password):
            raise exceptions.NotFound()

        self.user = user
        return data
    
    def save(self, *args, **kwargs):
        return Token.objects.create(user_id=self.user.id).key