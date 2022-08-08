from django.db import models
from django.urls import reverse

# Create your models here.

class Account(models.Model):
    name = models.CharField(max_length = 200)
    balance = models.DecimalField(decimal_places=2, max_digits=9)
    slug = models.SlugField(null=True)

    def __str__(self):
        return "{n}: {b}".format(n=self.name, b=self.balance)

    def get_absolute_url(self):
        return reverse("account_detail", kwargs={"slug": self.slug})