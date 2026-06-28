# from django.shortcuts import render
# from django.http import HttpResponse
from django.http import HttpResponseForbidden

from .models import Product, Contacts
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, View
from django.urls import reverse_lazy
from .forms import ProductForm
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import get_object_or_404, redirect


class ProductListView(ListView):
    model = Product
    template_name = 'catalog/home.html'
    context_object_name = 'products'


class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product_detail.html'
    context_object_name = 'product'


class ContactsListView(ListView):
    model = Contacts
    template_name = 'catalog/contacts.html'
    context_object_name = 'contacts'


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('catalog:product_list')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('catalog:product_list')
    permission_required = 'catalog.change_product'

    def has_permission(self):
        if super().has_permission():
            return True
        obj = self.get_object()  # self.get_object() достаёт продукт по pk из URL
        return self.request.user == obj.owner


    def get_success_url(self):
        return reverse_lazy('catalog:product_detail', args=[self.kwargs.get('pk')])


class ProductDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Product
    template_name = 'catalog/product_confirm_delete.html'
    success_url = reverse_lazy('catalog:product_list')
    permission_required = 'catalog.delete_product'

    def has_permission(self):
        if super().has_permission():
            return True
        obj = self.get_object()  # self.get_object() достаёт продукт по pk из URL
        return self.request.user == obj.owner

class PublishProductView(LoginRequiredMixin, View):
    def post(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        if not request.user.has_perm('catalog.can_unpublish_product'):
            return HttpResponseForbidden('У вас нет прав на публикацию продукта')

        if product.is_published:
            product.is_published = False
        else:
            product.is_published = True
        product.save()
        return redirect('catalog:product_list')


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
