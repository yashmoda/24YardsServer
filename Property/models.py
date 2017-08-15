from __future__ import unicode_literals

from django.db import models

# Create your models here.
from HomeScreen.models import PropertyType


class PropertyTable(models.Model):
    property_type = models.ForeignKey(PropertyType, db_column='PropertyType.id')
    title = models.CharField(max_length=20)
    location = models.TextField()
    bhk = models.IntegerField()
    description = models.TextField()
    price = models.IntegerField()
    contact = models.CharField(max_length=10)
    usage = models.CharField(max_length=20, default=None)
    date_added = models.DateField()
    #image = models.ForeignKey(PropertyImage, db_column='PropertyImage.id')


class PropertyImage(models.Model):
    property = models.ForeignKey(PropertyTable, db_column='PropertyTable.id')
    image = models.ImageField(upload_to='images/')
