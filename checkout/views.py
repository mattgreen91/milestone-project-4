from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    basket = request.session.get('basket', {})
    if not basket:
        messages.error(request, "There's nothing in your basket at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51JhyYaJrOAqO2sMfX3BUSHsXwVOl6zOU6gZId6T3ZQuGPr1staRvIFEBfuh6fItx4MY5Gd2RqrKOqCIhOVlwYSeS00sXo1K6oz',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
