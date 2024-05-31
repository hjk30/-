from django.db import models


class Vendor(models.Model):
    name = models.CharField(max_length=200, null=False)
    surname = models.CharField(max_length=200, null=False)
    phone = models.CharField(max_length=20, null=False)
    salary = models.IntegerField(null=False)

    @property
    def fio(self):
        return f'{self.name} {self.surname}'

    def __str__(self):
        return f'{self.fio} ({self.phone})'

    def __repr__(self):
        return f'Vendor(name="{self.name}", surname="{self.surname}", phone="{self.phone}")'
