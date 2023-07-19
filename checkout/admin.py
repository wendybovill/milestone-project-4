from django.contrib import admin
from .models import Order, OrderLineItem


class OrderLineItemAdminInline(admin.TabularInline):
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemAdminInline,)

    readonly_fields = ('order_number', 'date',
                       'delivery_cost', 'order_total',
                       'full_total', 'original_basket',
                       'stripe_pid', 'grand_total',)

    fields = ('order_number', 'user_profile', 'date',
              'first_name', 'last_name', 'street_address1',
              'street_address2', 'town_or_city', 'postcode',
              'county', 'country', 'email', 'phone_number',
              'delivery_cost', 'order_total', 'full_total',
              'original_basket', 'stripe_pid',)

    list_display = ('order_number', 'user_profile', 'date',
                    'first_name', 'last_name', 'street_address1',
                    'street_address2', 'town_or_city', 'postcode',
                    'county', 'country', 'email', 'phone_number',
                    'delivery_cost', 'order_total', 'full_total',
                    'original_basket', 'stripe_pid',)

    ordering = ('-date',)  # new orders at the top


admin.site.register(Order, OrderAdmin)
