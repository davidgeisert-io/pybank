from django.db import models
from django.urls import reverse

# Create your models here.

class Account(models.Model):
    name = models.CharField(max_length = 200, unique=True)
    balance = models.DecimalField(default=0, decimal_places=2, max_digits=9)

    def __str__(self):
        return "{n}: {b}".format(n=self.name, b=self.balance)
        