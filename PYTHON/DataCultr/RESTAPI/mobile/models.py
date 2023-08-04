from django.db import models

# Create your models here.


class Brand(models.Model):
   name = models.CharField(max_length=100)
   created = models.DateField(null=True)
   company_name = models.CharField(max_length=100)


class Model(models.Model):
   name = models.CharField(max_length=100)
   price = models.CharField(max_length=10)
   launch_date = models.DateField(null=True)
   brand = models.ForeignKey(Brand, on_delete=models.DO_NOTHING)
