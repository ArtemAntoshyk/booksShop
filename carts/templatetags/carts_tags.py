from django import template

from carts.models import Cart
from carts.utils import get_user_carts
from carts.utils import get_user_orders

register = template.Library()


@register.simple_tag()
def user_carts(request):
    return get_user_carts(request)


@register.simple_tag()
def user_orders(request):
    return get_user_orders(request)
