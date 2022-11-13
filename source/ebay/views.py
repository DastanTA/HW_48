from django.shortcuts import render
from ebay.models import Product, CATEGORY_CHOICES

def main_page(request):
    products = Product.objects.all().order_by("category", "name").filter(remainder__gt=0)
    context = {'products': products}
    return render(request, 'index.html', context)
