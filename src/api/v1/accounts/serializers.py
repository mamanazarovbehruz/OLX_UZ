from rest_framework import serializers, exceptions
from rest_framework.authtoken.models import Token
# from rest_framework.exceptions import ValidationError

from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.db.models import Q

from .models import CustomUser
from .validators import validate_phone


class StaffRegisterSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ['username', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }
    
    def validate(self, attrs):
        try:
            validate_email(attrs['username'])
            attrs['email'] = attrs['username']
        except:
            try:
                validate_phone(attrs['username'])
                attrs['phone_number'] = attrs['username']
            except:
                raise ValidationError('Enter valid email or phone number')
            
        user = CustomUser.objects.filter(
            Q(username=attrs['username']) | Q(email=attrs['username']) |
            Q(phone_number=attrs['username'])
        ).exists()
        
        if user:
            raise exceptions.ValidationError('This user already created')
        
        return attrs


    def create(self, validated_data):
        instance = CustomUser.objects.create_user(is_staff=True, **validated_data)
        return instance
    

class ClientRegisterSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ['username', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def validate(self, attrs):
        try:
            validate_email(attrs['username'])
            attrs['email'] = attrs['username']
        except:
            try:
                validate_phone(attrs['username'])
                attrs['phone_number'] = attrs['username']
            except:
                raise ValidationError('Enter valid email or phone number')
            
        user = CustomUser.objects.filter(
            Q(username=attrs['username']) | Q(email=attrs['username']) |
            Q(phone_number=attrs['username'])
        ).exists()
        
        if user:
            raise exceptions.ValidationError('This user already created')
        
        return attrs

    def create(self, validated_data):
        instance = CustomUser.objects.create_user(**validated_data)
        return instance


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


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('number_id', 'username', 'avatar')