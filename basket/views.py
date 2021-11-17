from django.shortcuts import (
    render, redirect, reverse, HttpResponse, get_object_or_404)
from django.contrib import messages

from products.models import Product

# Create your views here.


def view_basket(request):
    """ A view that renders the basket contents page """

    return render(request, 'basket/basket.html')


def add_to_basket(request, product_sku):
    """ Add a quantity of the specified product to the shopping basket """

    product = get_object_or_404(Product, sku=product_sku)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    print(redirect_url)
    basket = request.session.get('basket', {})

    if product_sku in list(basket.keys()):
        basket[product_sku] += quantity
        messages.success(
            request, f'Changed {product.name} quantity to \
            {basket[product_sku]}')
    else:
        basket[product_sku] = quantity
        messages.success(request, f'Added {product.name} to your basket')

    request.session['basket'] = basket
    print(request.session['basket'])
    return redirect(redirect_url)


def modify_basket(request, product_sku):
    """Adjust the quantity of the specified product to the specified amount"""

    product = get_object_or_404(Product, sku=product_sku)
    quantity = int(request.POST.get('quantity'))
    basket = request.session.get('basket', {})

    if quantity > 0:
        basket[product_sku] = quantity
        messages.success(
            request, f'Changed {product.name} quantity to \
            {basket[product_sku]}')
    else:
        basket.pop(product_sku)
        messages.success(request, f'Removed {product.name} from your basket')

    request.session['basket'] = basket
    return redirect(reverse('view_basket'))


def remove_from_basket(request, product_sku):
    """Remove the item from the shopping basket"""

    try:
        product = get_object_or_404(Product, sku=product_sku)
        basket = request.session.get('basket', {})
        basket.pop(product_sku)
        messages.success(request, f'Removed {product.name} from your basket')

        request.session['basket'] = basket
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item {e}')
        return HttpResponse(status=500)
