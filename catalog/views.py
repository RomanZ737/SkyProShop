from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'catalog/home.html')


def contacts(request):
    if request.method == "POST":
        name = request.POST['name']
        phone = request.POST['phone']
        message = request.POST['message']
        return HttpResponse(f'Уважаемый, {name}, Ваше сообщение получено\n'
                            f'Мы свяжемся с вами по телефону: {phone}')
    return render(request, 'catalog/contacts.html')


