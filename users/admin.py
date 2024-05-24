from django.contrib import admin
from carts.admin import CartTabAdmin
# from orders.admin import OrderTabulareAdmin

from users.models import Client


# admin.site.register(User)

@admin.register(Client)
class UserAdmin(admin.ModelAdmin):
    list_display = ["username", "phone",  "email", ]
    search_fields = ["username", "phone",  "email", ]

    inlines = [CartTabAdmin, ]