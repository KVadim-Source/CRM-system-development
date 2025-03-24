from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required
from .models import Product
from .forms import ProductForm


@permission_required('products.view_product')
def product_list(request):
    products = Product.objects.all()
    return render(request, 'products-list.html', {'products': products})


@permission_required('products.add_product')
def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('products:product_list')
    else:
        form = ProductForm()
    return render(request, 'products-create.html', {'form': form})


@permission_required('products.view_product')
def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'products-detail.html', {'object': product})


@permission_required('products.change_product')
def product_update(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('products:product_detail', pk=product.pk)
    else:
        form = ProductForm(instance=product)
    return render(request, 'products-edit.html', {'form': form, 'object': product})


@permission_required('products.delete_product')
def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('products:product_list')
    return render(request, 'products-delete.html', {'object': product})
