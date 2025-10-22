from django.shortcuts import render

from .models import Product, TextList, ProductSeo, Point


def product_page(request, product_id):
    products = Product.objects.get(pk=product_id)
    text_lists = TextList.objects.all().prefetch_related('points')
    points = Point.objects.all()
    product_seo = ProductSeo.objects.last()

    context = {
        'products': products,
        'text_lists': text_lists,
        'points': points,
        'product_seo': product_seo,
    }
    return render(request, 'product.html', context)
