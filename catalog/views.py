# from django.shortcuts import render
# from django.http import HttpResponse
from .models import Product, Contacts
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import ProductForm
from django.contrib.auth.mixins import LoginRequiredMixin


class ProductListView(ListView):
    model = Product
    template_name = 'catalog/home.html'
    context_object_name = 'products'


class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product_detail.html'


class ContactsListView(ListView):
    model = Contacts
    template_name = 'catalog/contacts.html'
    context_object_name = 'contacts'


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('catalog:product_list')




class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('catalog:product_list')

    def get_success_url(self):
        return reverse_lazy('catalog:product_detail', args=[self.kwargs.get('pk')])


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    template_name = 'catalog/product_confirm_delete.html'
    success_url = reverse_lazy('catalog:product_list')


# def home(request):
#     products = Product.objects.all()
#     context = {'products': products}
#     return render(request, 'catalog/home.html', context)
#
#
# def contacts(request):
#     if request.method == "POST":
#         name = request.POST['name']
#         phone = request.POST['phone']
#         message = request.POST['message']
#         return HttpResponse(f'Уважаемый, {name}, Ваше сообщение получено\n'
#                             f'Мы свяжемся с вами по телефону: {phone}')
#     contacts = Contacts.objects.first()
#     print(contacts.country, contacts.tax_num, contacts.address)
#     return render(request, 'catalog/contacts.html',
#                   context={'country': contacts.country,
#                            'tax_num': contacts.tax_num,
#                            'address': contacts.address,})
#
# def product_detail(request, product_id):
#     print(product_id)
#     test = Product.objects.all()
#     for product in test:
#         print(product.id)
#     product = Product.objects.get(id=product_id)
#
#     context = {'product': product}
#     return render(request, 'catalog/product_detail.html', context=context)
#
