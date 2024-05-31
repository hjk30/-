from django.contrib import admin

from django_project import models

admin.site.register(models.Vendor)
admin.site.register(models.Customer)
admin.site.register(models.Purchase)
