from django.urls import path
from .views import RegisterView, CustomLoginView, CustomLogoutView, UserUpdateView
from users.apps import UsersConfig


app_name = UsersConfig.name

urlpatterns = [
    path('users/login/', CustomLoginView.as_view(template_name='users/login.html'), name='login'),
    path('users/', CustomLogoutView.as_view(next_page='/'), name='logout'),
    path('users/register/', RegisterView.as_view(), name='register'),
    path('users/update/', UserUpdateView.as_view(), name='user_update'),
]