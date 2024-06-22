from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
from .forms import ProductForm


def product_list(request):
    sort_by = request.GET.get('sort', 'asc')
    if sort_by == 'desc':
        products = Product.objects.all().order_by('-price')
    else:
        products = Product.objects.all().order_by('price')

    paginator = Paginator(products, 15)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'app/product_list.html', {'page_obj': page_obj, 'sort_by': sort_by})

def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'app/product_form.html', {'form': form})

def product_update(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm(instance=product)
    return render(request, 'app/product_form.html', {'form': form})

def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('product_list')
    return render(request, 'app/product_confirm_delete.html', {'product': product})