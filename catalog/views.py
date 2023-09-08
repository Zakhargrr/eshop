from django.shortcuts import render

from catalog.models import Product


# Create your views here.
def home(request):
    products_list = Product.objects.all()
    context = {
        'object_list': products_list
    }
    return render(request, 'catalog/home.html', context)


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print("\nКонтактные данные пользователя:")
        print(f"Имя: {name}")
        print(f"Телефон: {phone}")
        print(f"Сообщение: {message}\n")
    return render(request, 'catalog/contacts.html')


def product(request):
    products_list = Product.objects.all()
    context = {
        'object_list': products_list,
    }
    return render(request, 'catalog/product.html', context)
