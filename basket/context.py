from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product

def basket_contents(request):

    basket_products = []
    total = 0
    product_count = 0
    basket = request.session.get('basket', {})

    for product_sku, product_data in basket.items():
        if isinstance(product_data, int):
            product = get_object_or_404(Product, sku=product_sku)
            total += product_data * product.selling_price
            product_count += product_data
            basket_products.append({
                'product_sku': product_sku,
                'quantity': product_data,
                'product': product,
            })

    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = 0
        free_delivery_delta = 0
    
    grand_total = delivery + total
    
    context = {
        'basket_products': basket_products,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
    }

    return context
