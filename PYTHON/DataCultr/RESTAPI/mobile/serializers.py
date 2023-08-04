from rest_framework import serializers
from mobile.models import Brand, Model

class ModelSerializer(serializers.ModelSerializer):
   class Meta:
       model = Model
       fields = ('name', 'price', 'launch_date', 'brand')


class BrandSerializer(serializers.ModelSerializer):
   class Meta:
       model = Brand
       fields = ('name', 'created', 'company_name')