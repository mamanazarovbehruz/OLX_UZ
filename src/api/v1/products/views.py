from rest_framework import (
    generics,
    permissions,
    authentication
)

import django_filters.rest_framework
from django.db.models import Q
from api.v1.accounts.permissions import IsDeleted
from .models import *
from .enums import Status
from .serializers import *


class CategoryAdminListCreateAPIView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryAdminSerializer
    permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]
    authentication_classes = [authentication.BasicAuthentication]

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)      


class CategoryAdminRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryAdminSerializer
    permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]
    authentication_classes = [authentication.BasicAuthentication]

    def perform_destroy(self, instance):
        instance.is_deleted = True
        instance.save()

class CategoryClientListAPIView(generics.ListAPIView):
    queryset = Category.objects.filter(is_active=True)
    serializer_class = CategoryClientSerializer


class FieldAdminListCreateAPIView(generics.ListCreateAPIView):
    queryset = Field.objects.all()
    serializer_class = FieldAminSerializer
    permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]
    authentication_classes = [authentication.BasicAuthentication]

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)


class FieldAdminRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Field.objects.all()
    serializer_class = FieldAminSerializer
    permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]
    authentication_classes = [authentication.BasicAuthentication]

    def perform_destroy(self, instance):
        instance.is_deleted = True
        instance.save()


class FieldClientListAPIView(generics.ListAPIView):
    queryset = Field.objects.filter(is_active=True)
    serializer_class = FieldSerializer


class ProductCreateAPIView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductCreateSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.BasicAuthentication]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class ProductRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductRetrieveUpdateDestroySerializer
    permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]
    authentication_classes = [authentication.BasicAuthentication]

    def perform_destroy(self, instance):
        instance.is_deleted = True
        instance.save()


class ProductClientListAPIView(generics.ListAPIView):
    queryset = Product.objects.filter(status=Status.a.name, is_deleted=False)
    serializer_class = ProductListSerializer


class ProductDetailListAPIView(generics.ListAPIView):
    queryset = Product.objects.filter(status=Status.a.name, is_deleted=False)
    serializer_class = ProductDetailSerializer

class ProductFieldCreateAPIView(generics.CreateAPIView):
    queryset = ProductField.objects.all()
    serializer_class = ProductFieldSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.BasicAuthentication]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class ProductFieldRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProductField.objects.all()
    serializer_class = ProductFieldSerializer
    permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]
    authentication_classes = [authentication.BasicAuthentication]

    def perform_destroy(self, instance):
        instance.is_deleted = True
        instance.save()