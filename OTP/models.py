from __future__ import unicode_literals

from django.db import models

# Create your models here.
class OTP(models.Model):
    phone = models.CharField(max_length=10)
    otp = models.CharField(max_length=6)

    def __str__(self):
        return str(self.phone)