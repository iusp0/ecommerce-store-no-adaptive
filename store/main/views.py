from django.db.models import Q

from django.shortcuts import render, HttpResponseRedirect
from django.core.paginator import Paginator
from django.contrib import messages
from django.urls import reverse


from .models import Product, ProductCategory
from users.forms import CartForm, QuestionsForm

# Create your views here.
def home(request):
    if request.method == 'POST':
        form = QuestionsForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Ваш вопрос успешно отправлен!')
            return HttpResponseRedirect(reverse('main:bardStore'))
        else:
            print('error')
    else:
        form = QuestionsForm()
    context = {
        'title': 'Bard Store',
        'form': form
    }
    return render(request, 'main/index.html', context)


def products(request, category_id=None, page_number=1):
    categories = ProductCategory.objects.all()
    products = Product.objects.all()

    # Фильтрация по категории
    if category_id:
        products = products.filter(category_id=category_id)

    # Обработка поискового запроса
    search_query = request.GET.get('s')
    if search_query:
        search_query = search_query.capitalize()
        products = products.filter(Q(name__icontains=search_query) | Q(name__iexact=search_query))

    per_page = 4
    paginator = Paginator(products, per_page)
    products_paginator = paginator.page(page_number)

    context = {
        'products': products_paginator,
        'categories': categories,
        'current_page': page_number,
        'category_id': category_id,
        'search_query': search_query,
    }
    return render(request, 'main/products.html', context)


def product(request, product_id):
    form = CartForm()
    product = Product.objects.get(id=product_id)
    context = {
        'product': product,
        'form': form
    }
    return render(request, 'main/product.html', context)
