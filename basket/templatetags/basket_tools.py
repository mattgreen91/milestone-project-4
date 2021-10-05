from django import template


register = template.Library()


@register.filter(name='calc_subtotal')
def calc_subtotal(selling_price, quantity):
    return selling_price * quantity
