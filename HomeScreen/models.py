from __future__ import unicode_literals

from django.db import models

# Create your models here.


class PropertyType(models.Model):
    property_type = models.CharField(max_length=20)
    message = models.TextField()
    image = models.ImageField(upload_to='static/')

    def __str__(self):
        return self.property_type
