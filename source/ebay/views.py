from django.shortcuts import render, get_object_or_404
from ebay.models import Product


def main_page(request):
    products = Product.objects.all().order_by("category", "name").filter(remainder__gt=0)
    context = {'products': products}
    return render(request, 'index.html', context)


def view_product(request, pk, *args, **kwargs):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'product.html', {'product': product})


def create_product(request, pk, *args, **kwargs):
    pass


def update_product(request, pk, *args, **kwargs):
    pass


def delete_product(request, pk, *args, **kwargs):
    pass
