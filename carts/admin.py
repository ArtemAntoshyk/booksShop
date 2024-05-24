from django.contrib import admin

from carts.models import Cart

# admin.site.register(Cart)
from django.contrib import admin
from .models import Cart


class CartTabAdmin(admin.TabularInline):
    model = Cart
    fields = "book", "quantity", "created_timestamp"
    search_fields = "book", "quantity", "created_timestamp"
    readonly_fields = ("created_timestamp",)
    extra = 1


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ["user_display", "book_display", "quantity", "created_timestamp"]
    list_filter = ["created_timestamp", "client", "book"]

    def user_display(self, obj):
        if obj.client:
            return str(obj.client)
        return "Анонимный пользователь"

    def book_display(self, obj):
        return str(obj.book.name_book)
