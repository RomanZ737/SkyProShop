from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView
from .forms import CustomUserCreationForm
from django.core.mail import send_mail
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import CustomUser
from django.contrib.auth import login
from catalog.services import CategoryService


class CustomLoginView(LoginView):
    template_name = 'users/login.html'
    success_url = reverse_lazy('catalog:product_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category_list'] = CategoryService.get_category_list()
        return context



class CustomLogoutView(LogoutView):
    def get_next_page(self):
        return reverse_lazy('login')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category_list'] = CategoryService.get_category_list()
        return context


class RegisterView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('catalog:product_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category_list'] = CategoryService.get_category_list()
        return context


    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        self.send_welcome_email(user.email)
        return super().form_valid(form)

    def send_welcome_email(self, user_email):
        print('Email: ', user_email)
        subject = 'Добро пожаловать в наш сервис'
        message = 'Спасибо, что зарегистрировались в нашем сервисе!'
        recipient_list = [user_email]
        from_email = 'pomanz@mail.ru'
        try:
            send_mail(subject, message, from_email, recipient_list)
        except Exception as e:
            print(e)


class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = CustomUser
    fields = ['username', 'email', 'phone_number']
    template_name = 'users/register.html'
    success_url = reverse_lazy('catalog:product_list')


    def get_object(self, queryset=None):
        return self.request.user

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category_list'] = CategoryService.get_category_list()
        return context