from django.shortcuts import render

from DjangoECommerceStore.settings import PAYPAL_ID
from .models import ShippingAddress

import environ


def payment_success(request):
    return render(request, 'payment/payment-success.html')


def payment_failed(request):
    return render(request, 'payment/payment-failed.html')


def checkout(request):
    context = {'pay_pal_id': PAYPAL_ID}
    if request.user.is_authenticated:
        try:
            # User with shipping info
            shipping_address = ShippingAddress.objects.get(user=request.user.id)
            context['shipping'] = shipping_address
            return render(request, 'payment/checkout.html', context=context)
        except ShippingAddress.DoesNotExist:
            # User without shipping info
            return render(request, 'payment/checkout.html', context=context)

    # Guest users
    return render(request, 'payment/checkout.html', context=context)


def complete_order(request):
    pass
