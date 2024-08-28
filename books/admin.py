from django.contrib import admin

from books.models import Genres, Books, BooksAndTheirGenre


# admin.site.register(Categories)
# admin.site.register(Products)


@admin.register(Genres)
class GenresAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("genre_name",)}
    list_display = ["genre_name",]

@admin.register(Books)
class BooksAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name_book",)}
    list_display = ["name_book", "page_amount", "year_production", "price",]
    list_editable = ["price",]
    search_fields = ["name_book",]
    list_filter = ["price", "year_production", ]
    fields = [
        "id",
        "name_book",
        "slug",
        "description",
        "image",
        "page_amount",
        "year_production",
        "author",
        "price"
    ]

@admin.register(BooksAndTheirGenre)
class BooksAndTheirGenreModel(admin.ModelAdmin):
    fields = [
        "book",
        "genre"
    ]