# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class ContactForm(models.Model):
    property_title = models.CharField(max_length=100)
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=10)

    def __str__(self):
        return self.name