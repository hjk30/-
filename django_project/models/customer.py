from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=20, null=False)
    phone = models.CharField(max_length=20, null=False)

    def __str__(self):
        return self.name

    def __repr__(self):
        return f'Customer(name="{self.name}", phone="{self.phone}")'
