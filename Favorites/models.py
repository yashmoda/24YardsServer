# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
# Create your models here.
class Favorite(models.Model):
    property = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)

    def __str__(self):
        return str(self.phone)
