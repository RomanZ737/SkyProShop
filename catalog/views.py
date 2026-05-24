from django.shortcuts import render
from django.http import HttpResponse
from .models import Product, Contacts


def home(request):
    for product in Product.objects.all().order_by('-created_at')[:5]:
        print(product.name)
    return render(request, 'catalog/home.html')


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


