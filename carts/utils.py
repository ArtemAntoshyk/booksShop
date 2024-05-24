from carts.models import Cart
from orders.models import Order
from users.models import Client


def get_user_carts(request):
    print(request.user)
    print(request.user.is_authenticated)
    print(request.session.session_key)

    if request.user.is_authenticated:
        client_id = Client.objects.get(username=request.user)
        #
        print(f"id in get_user_carts: {client_id}")
        # print(client_id.id)
        #
        # print(Cart.objects.get(client=client_id))
        # print(Cart.objects.filter(client=client_id))
        return Cart.objects.filter(client=client_id).select_related("book")

    if not request.session.session_key:
        request.session.create()

    return Cart.objects.filter(session_key=request.session.session_key).select_related('book')


def get_user_orders(request):
    print(request.user)
    print(request.user.is_authenticated)
    print(request.session.session_key)

    if request.user.is_authenticated:
        client_id = Client.objects.get(username=request.user)
        #
        print(f"id in get_user_carts: {client_id}")
        # print(client_id.id)
        #
        # print(Cart.objects.get(client=client_id))
        # print(Cart.objects.filter(client=client_id))
        return Order.objects.filter(user=client_id)

