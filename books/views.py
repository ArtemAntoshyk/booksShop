from django.shortcuts import render

# Create your views here.
from django.core.paginator import Paginator
from django.shortcuts import get_list_or_404, get_object_or_404, render

from .models import *


def catalog(request, genre_slug=None):
    page = request.GET.get('page', 1)
    on_sale = request.GET.get('on_sale', None)
    order_by = request.GET.get('order_by', None)
    query = request.GET.get('q', None)

    if genre_slug == "all":
        books = Books.objects.all()
    elif query:
        books = Books.objects.filter(name_book__icontains=query)
    else:
        genre = get_object_or_404(Genres, slug=genre_slug)
        books_and_genre = BooksAndTheirGenre.objects.filter(genre=genre)
        books = Books.objects.filter(id__in=books_and_genre.values('book_id'))
    if on_sale:
        books = books.filter(discount__gt=0)

    if order_by and order_by != "default":
        books = books.order_by(order_by)

    paginator = Paginator(books, 3)
    current_page = paginator.page(int(page))

    context = {
        "title": "Home - Catalog",
        "books": current_page,
        "slug_url": genre_slug
    }
    return render(request, "books/catalog.html", context)


def book_detail(request, books_slug):
    books = Books.objects.get(slug=books_slug)

    context = {"books": books}
    print(books.image)
    return render(request, "books/product.html", context=context)
