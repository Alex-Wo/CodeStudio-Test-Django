from django.contrib import admin
from django.utils.safestring import mark_safe
from nested_admin import NestedModelAdmin, NestedTabularInline

from .models import Product, TextList, ProductSeo, Point


class PointAdmin(NestedTabularInline):
    model = Point
    extra = 1
    fields = ['text']


class TextListAdmin(NestedTabularInline):
    model = TextList
    inlines = [PointAdmin]
    extra = 1
    fields = ['title']


class ProductSeoAdmin(NestedTabularInline):
    model = ProductSeo
    extra = 1
    fields = ['keywords', 'description']


@admin.register(Product)
class ProductAdmin(NestedModelAdmin):
    list_display = ['title', 'alt', 'image_thumbnail']
    inlines = [TextListAdmin, ProductSeoAdmin]
    search_fields = 'title',

    def image_thumbnail(self, obj):
        if obj.image:
            return mark_safe(f"<img src='{obj.image.url}' height='120px' width=170>")
        else:
            return 'Нет изображения'

    image_thumbnail.short_description = 'Изображение'
