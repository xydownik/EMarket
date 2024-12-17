from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils.timezone import now

from api.models import Order


class Payment(models.Model):
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
    payment_method= models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=0)
    status = models.CharField(max_length=255)
    created_at = models.DateTimeField(default=now)
    updated_at = models.DateTimeField(auto_now=True)
