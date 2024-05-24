from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.template.loader import render_to_string
from users.models import Client
from carts.models import Cart
from carts.utils import get_user_carts

from books.models import Books


def cart_add(request):
    print(request.POST)
    book_id = request.POST.get("book_id")
    print(book_id)
    book = Books.objects.get(id=book_id)
    print(f"{book.name_book}  {book.id} {book.slug}")
    print(request.user)
    if request.user.is_authenticated:
        client = Client.objects.get(username=request.user)
        print(f"id: {client.id}")
        carts = Cart.objects.filter(client=client, book=book)
        print(f"{book.name_book.encode('utf-8', 'ignore').decode('utf-8')}  {book.id} {book.slug}")

        if carts.exists():
            cart = carts.first()
            if cart:
                cart.quantity += 1
                cart.save()
        else:
            Cart.objects.create(client=client, book=book, quantity=1)

    else:
        carts = Cart.objects.filter(session_key=request.session.session_key, book=book)
        print(carts)
        if carts.exists():
            cart = carts.first()
            if cart:
                cart.quantity += 1
                cart.save()
        else:
            print(request.session.session_key)
            Cart.objects.create(session_key=request.session.session_key, book=book, quantity=1)

    user_cart = get_user_carts(request)
    return render(
        request=request, template_name="users/users_cart.html", context={"carts": user_cart}, )
    # cart_items_html = render_to_string(
    #     "carts/includes/included_cart.html", {"carts": user_cart}, request=request)

    # response_data = {
    #     "message": "Товар добавлен в корзину",
    #     "cart_items_html": cart_items_html,
    # }
    #
    # return JsonResponse(response_data)


def cart_change(request):
    cart_id = request.POST.get("cart_id")
    action = request.POST.get("action")
    cart = Cart.objects.get(id=cart_id)

    if action == "increment":
        cart.quantity += 1
    elif action == "decrement" and cart.quantity > 1:
        cart.quantity -= 1

    cart.save()

    carts = get_user_carts(request)
    return render(
        request=request, template_name="users/users_cart.html", context={"carts": carts},
    )


def cart_remove(request):
    cart_id = request.POST.get("cart_id")
    print(cart_id)
    cart = Cart.objects.get(id=cart_id)
    quantity = cart.quantity
    cart.delete()

    user_cart = get_user_carts(request)
    cart_items_html = render_to_string(
        "carts/includes/included_cart.html", {"carts": user_cart}, request=request)

    response_data = {
        "message": "Товар удален",
        "cart_items_html": cart_items_html,
        "quantity_deleted": quantity,
    }

    return render(
        request=request, template_name="users/users_cart.html", context={"carts": user_cart}, )
    # cart_items_html = render_to_string(
    #     "carts/includes/included_cart.html", {"carts": user_cart}, request=request)

    # response_data = {
    #     "message": "Товар добавлен в корзину",
    #     "cart_items_html": cart_items_html,
    # }
    #
    # return JsonResponse(response_data)
