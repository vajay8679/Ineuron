from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets
from mobile.serializers import ModelSerializer, BrandSerializer
from mobile.models import Model, Brand


class ModelViewSet(viewsets.ModelViewSet):
   queryset = Model.objects.all()
   serializer_class = ModelSerializer


class BrandViewSet(viewsets.ModelViewSet):
   queryset = Brand.objects.all()
   serializer_class = BrandSerializer
