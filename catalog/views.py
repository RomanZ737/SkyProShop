from django.shortcuts import render
from django.http import HttpResponse
from .models import Product, Contacts


def home(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'catalog/home.html', context)


def contacts(request):
    if request.method == "POST":
        name = request.POST['name']
        phone = request.POST['phone']
        message = request.POST['message']
        return HttpResponse(f'Уважаемый, {name}, Ваше сообщение получено\n'
                            f'Мы свяжемся с вами по телефону: {phone}')
    contacts = Contacts.objects.first()
    print(contacts.country, contacts.tax_num, contacts.address)
    return render(request, 'catalog/contacts.html',
                  context={'country': contacts.country,
                           'tax_num': contacts.tax_num,
                           'address': contacts.address,})

def product_detail(request, product_id):
    print(product_id)
    test = Product.objects.all()
    for product in test:
        print(product.id)
    product = Product.objects.get(id=product_id)

    context = {'product': product}
    return render(request, 'catalog/product_detail.html', context=context)

