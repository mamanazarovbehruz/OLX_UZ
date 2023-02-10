from rest_framework import (
    generics,
    permissions,
    authentication,
    response,
)

from .permissions import IsDeleted
from .models import CustomUser
from .serializers import *

# Create your views here.

class StaffRegisterAPIView(generics.CreateAPIView):
    serializer_class = StaffRegisterSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.BasicAuthentication]


class ClientRegisterAPIView(generics.CreateAPIView):
    serializer_class = ClientRegisterSerializer


class UserRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.filter(is_deleted=False)
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated, ~IsDeleted]
    authentication_classes = (authentication.TokenAuthentication)

    def get_object(self):
        return self.request.user
    
    def perform_destroy(self, instance):
        instance.is_deleted = True
        instance.save()


class UserLoginAPIView(generics.CreateAPIView):
    serializer_class = UserLoginSerializer

    def create(self, request, *args, **kwargs):
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        token = serializer.save()
        return response.Response({'token': token}, status=201)