from django.db import models

from .vendor import Vendor
from .customer import Customer


class Purchase(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.CharField(max_length=200, null=False)
    quantity = models.IntegerField(null=False)
    price = models.IntegerField(null=False)

    def __str__(self):
        return f'{self.vendor.fio}: {self.customer} -> {self.product}'

    def __repr__(self):
        return f'Purchase(vendor="{self.vendor}", customer="{self.customer}", {self.quantity} product="{self.product}")'
