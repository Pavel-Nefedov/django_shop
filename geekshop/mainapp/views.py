from django.shortcuts import render, get_object_or_404

# Create your views here.
from basketapp.models import Basket
from mainapp.models import ProductCategory, Product


#link_menu заменил на categories
def products(request, pk=None):
    title = 'каталог'
    categories = ProductCategory.objects.all()
    basket = []
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)

    if pk is not None:
        if pk == 0:
            products = Product.objects.all().order_by('price')
            category = {'name' : 'Все'}
        else:
            category = get_object_or_404(ProductCategory, pk=pk)
            products = Product.objects.filter(category__pk=pk).order_by('price')

        context = {
            'title': title,
            'categories' : categories,
            'products' : products,
            'category' : category,
            'basket': basket,
        }

        return render(request, 'mainapp/products.html', context)

    same_products = Product.objects.all()

    context = {
        'title': title,
        'categories': categories,
        'products': same_products,
        'basket': basket,
    }

    return render(request, 'mainapp/products.html', context)