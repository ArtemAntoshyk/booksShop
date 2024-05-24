from django.urls import path

from books import views

app_name = 'books'

urlpatterns = [
    path('search/', views.catalog, name='search'),
    path('<slug:genre_slug>/', views.catalog, name='index'),
    path('product/<slug:books_slug>/', views.book_detail, name='product'),
]