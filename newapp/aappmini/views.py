from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Manufacturer, Product
from .serializers import ManufacturerSerializer, ProductSerializer

class ManufacturerViewSet(ModelViewSet):
    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerSerializer 

class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer