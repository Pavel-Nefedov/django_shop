from django.shortcuts import render

# Create your views here.
from mainapp.models import ProductCategory, Product


#link_menu заменил на categories
def products(request):
    title = 'каталог'
    categories = ProductCategory.objects.all()
    # links_menu = [
    #     {'href': 'products_all', 'name': 'все'},
    #     {'href': 'products_home', 'name': 'дом'},
    #     {'href': 'products_office', 'name': 'офис'},
    #     {'href': 'products_modern', 'name': 'модерн'},
    #     {'href': 'products_classic', 'name': 'классика'},
    # ]

    context = {
        'title': title,
        # 'links_menu' : links_menu,
        'categories' : categories,

    }

    return render(request, 'mainapp/products.html', context)
