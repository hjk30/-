# -*- coding: utf-8 -*-
from collections import defaultdict

from django.views.generic.base import TemplateView

from .models import Purchase


class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        purchases = Purchase.objects.all()
        vendor_purchases = defaultdict(dict)

        customers = set()
        for purchase in purchases:
            customer_name = purchase.customer.name
            customers.add(customer_name)
            vendor_purchases[purchase.vendor][customer_name] = f'{purchase.product}, {purchase.quantity} шт. {purchase.price} руб.'

        customers = sorted(customers)
        vendor_statistics = [
            {
                'vendor': vendor,
                'purchases': [purchases[customer] for customer in customers]
            }
            for vendor, purchases in vendor_purchases.items()
        ]
        print(customers)
        context.update(
            {
                'customers': customers,
                'vendor_statistics': vendor_statistics
            }
        )
        return context
