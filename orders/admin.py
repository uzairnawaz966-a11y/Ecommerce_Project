from django.contrib import admin
from orders.models import Order, OrderItem

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = [
        "user",
        "address",
        "total_amount",
        "created_at"
    ]


@admin.register(OrderItem)
class OrderItemsAdmin(admin.ModelAdmin):
    list_display = [
        "order",
        "product",
        "quantity"
    ]