from django.contrib import admin
from .models import Category, Product, Slide, Season

"""
Defining classes for the Admin Views in the Superuser
login section
"""


class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ['image_preview',]
    list_display = (
        'name',
        'friendly_name',
        'tag',
        'discount',
        'image',
        'image_url',
        'description',
    )

    ordering = ('name',)


class SeasonAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'friendly_name',
    )

    ordering = ('name',)


class ProductAdmin(admin.ModelAdmin):
    readonly_fields = ['image_preview',]
    list_display = (
        'name',
        'sku',
        'image',
        'image_url',
        'price',
        'stock',
        'category',
        'tag',
        'friendly_name',
        'description',
        'hooksize',
        'colours',
        'discount',
        'specialoffer',
        'multipleproducts',
        'season',
    )

    ordering = ('name',)


class SlideAdmin(admin.ModelAdmin):
    readonly_fields = ['image_preview', 'image_path']
    list_display = (
        'name',
        'number',
        'title',
        'image',
        'image_url',
        'alt',
        'tag',
        'caption',
    )

    ordering = ('number',)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Season, SeasonAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Slide, SlideAdmin)
