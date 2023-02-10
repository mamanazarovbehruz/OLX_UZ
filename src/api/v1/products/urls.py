from django.urls import path
from .views import *

urlpatterns = [
    path('category/create', CategoryAdminListCreateAPIView.as_view()),
    path('category/<int:pk>/', CategoryAdminRetrieveUpdateDestroyAPIView.as_view()),
    path('categories/', CategoryClientListAPIView.as_view()),
    path('field/create/', FieldAdminListCreateAPIView.as_view()),
    path('field/<int:pk>/', FieldAdminRetrieveUpdateDestroyAPIView.as_view()),
    path('fields/', FieldClientListAPIView.as_view()),
    path('product/create/', ProductCreateAPIView.as_view()),
    path('product/<int:pk>/', ProductRetrieveUpdateDestroyAPIView.as_view()),
    path('product/detail/<int:pk>', ProductDetailListAPIView.as_view()),
    path('productfield/create/', ProductFieldCreateAPIView.as_view()),
    path('productfield/<int:pk>/', ProductFieldRetrieveUpdateDestroyAPIView.as_view()),
]
