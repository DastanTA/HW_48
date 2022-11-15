from django.shortcuts import render, get_object_or_404, redirect
from ebay.models import Product
from ebay.forms import ProductForm


def main_page(request):
    products = Product.objects.all().order_by("category", "name").filter(remainder__gt=0)
    context = {'products': products}
    return render(request, 'index.html', context)


def view_product(request, pk, *args, **kwargs):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'product.html', {'product': product})


def create_product(request, *args, **kwargs):
    if request.method == "GET":
        form = ProductForm()
        return render(request, 'create.html', {'form': form})
    elif request.method == "POST":
        form = ProductForm(data=request.POST)
        if form.is_valid():
            Product.objects.create(
                name=form.cleaned_data.get('name'),
                category=form.cleaned_data.get('category'),
                price=form.cleaned_data.get('price'),
                remainder=form.cleaned_data.get('remainder'),
                description=form.cleaned_data.get('description')
            )
            return redirect('main')
        else:
            return render(request, 'create.html', {'form': form})


def update_product(request, pk, *args, **kwargs):
    product = get_object_or_404(Product, pk=pk)
    if request.method == "GET":
        form = ProductForm(initial={
            'name': product.name,
            'category': product.category,
            'price': product.price,
            'remainder': product.remainder,
            'description': product.description
        })
        context = {'form': form, 'product': product}
        return render(request, 'update.html', context)
    elif request.method == "POST":
        form = ProductForm(data=request.POST)
        if form.is_valid():
            product.name = form.cleaned_data.get('name')
            product.category = form.cleaned_data.get('category')
            product.price = form.cleaned_data.get('price')
            product.remainder = form.cleaned_data.get('remainder')
            product.description = form.cleaned_data.get('description')
            product.save()
            return redirect('view_product', pk=product.pk)
        else:
            return render(request, 'update.html', {'form': form, 'product': product})


def delete_product(request, pk, *args, **kwargs):
    product = get_object_or_404(Product, pk=pk)
    if request.method == "GET":
        return render(request, 'delete.html', {'product': product})
    elif request.method == "POST":
        product.delete()
        return redirect('main')
