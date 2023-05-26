from django.shortcuts import render
from rest_framework import generics
from django.views.generic.list import ListView
from .models import Produits
from .serializers import ProductsListSerializer,ProductsDetailSerializer
from rest_framework.parsers import MultiPartParser, FormParser
# Create your views here.
from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.permissions import IsAuthenticated
from .models import Produits

from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import AllowAny
from .serializers import MyTokenObtainPairSerializer


class ProductsListAPIVIEW(generics.ListAPIView):
    queryset = Produits.objects.all()
    serializer_class=ProductsListSerializer
    parser_classes = (MultiPartParser, FormParser)
    permission_classes = [IsAuthenticated]

class MyObtainTokenPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = MyTokenObtainPairSerializer

class ProduitsRetrieveAPIVIEW(generics.RetrieveAPIView):
    lookup_field="id"
    queryset=Produits.objects.all()
    serializer_class = ProductsDetailSerializer
    parser_classes = (MultiPartParser, FormParser)


class ProduitsCreateAPIVIEW(generics.CreateAPIView):
    queryset = Produits.objects.all()
    serializer_class=ProductsDetailSerializer

class ProduitsRetrieveUpdateAPIVIEW(generics.UpdateAPIView):
    lookup_field="id"
    queryset=Produits.objects.all()
    serializer_class=ProductsDetailSerializer

class ProduitsDestroyAPIVIEW(generics.DestroyAPIView):
    lookup_field="id"
    queryset=Produits.objects.all()
    serializer_class=ProductsDetailSerializer