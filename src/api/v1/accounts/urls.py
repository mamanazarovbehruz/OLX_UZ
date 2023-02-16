from django.urls import path
from .views import *
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenBlacklistView, TokenVerifyView

urlpatterns = [
    path('register/staff/', StaffRegisterAPIView.as_view()),
    path('register/client/', ClientRegisterAPIView.as_view()),
    path('user/', UserRetrieveUpdateDestroyAPIView.as_view()),
    # path('login/', UserLoginAPIView.as_view()),
    path('login/', TokenObtainPairView.as_view()),
    path('access_update/', TokenRefreshView.as_view()),
    path('logout/', TokenBlacklistView.as_view()),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]
