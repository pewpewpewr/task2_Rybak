from django.db import models
from orders.models import Order

class Employee(models.Model):
    name = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, unique=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True, blank=True)
