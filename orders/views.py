from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db import transaction
from django.forms import ValidationError
from django.shortcuts import redirect, render

from carts.models import Cart
from users.models import Client

from orders.forms import CreateOrderForm
from orders.models import Order, OrderItem


@login_required
def create_order(request):
    if request.method == 'POST':
        form = CreateOrderForm(data=request.POST)
        if form.is_valid():
            try:
                with transaction.atomic():
                    user = request.user
                    client = Client.objects.get(username=user)
                    cart_items = Cart.objects.filter(client=client)

                    if cart_items.exists():
                        order = Order.objects.create(
                            user=user,
                            phone_number=form.cleaned_data['phone_number'],
                            requires_delivery=form.cleaned_data['requires_delivery'],
                            delivery_address=form.cleaned_data['delivery_address'],
                            payment_on_get=form.cleaned_data['payment_on_get'],
                        )
                        for cart_item in cart_items:
                            book=cart_item.book
                            name=cart_item.book.name_book
                            price=cart_item.book.sell_price()
                            quantity=cart_item.quantity

                            OrderItem.objects.create(
                                order=order,
                                book=book,
                                name=name,
                                price=price,
                                quantity=quantity,
                            )

                        cart_items.delete()

                        messages.success(request, 'Order complete')
                        return redirect('user:profile')
            except ValidationError as e:
                messages.success(request, str(e))
                return redirect('cart:order')
    else:
        initial = {
            'first_name': request.user.first_name,
            'last_name': request.user.last_name,
            }

        form = CreateOrderForm(initial=initial)

    context = {
        'title': 'Home - creat order',
        'form': form,
        'orders': True,
    }
    return render(request, 'orders/create_order.html', context=context)


@login_required
def order_details(request, order_id):
    order = Order.objects.get_object_or_404(Order, id=order_id, user=request.user)
    order_items = OrderItem.objects.filter(order=order)

    total_price = sum(item.price * item.quantity for item in order_items)
    total_quantity = sum(item.quantity for item in order_items)

    context = {
        'order': order,
        'order_items': order_items,
        'total_price': total_price,
        'total_quantity': total_quantity,
    }
    return render(request, 'users/profile.html', context=context)