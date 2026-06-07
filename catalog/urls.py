from django.urls import path
from . import views
from catalog.apps import CatalogConfig
from .views import ProductListView, ProductDetailView, ContactsListView

app_name = CatalogConfig.name


urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),

    path('contacts/', ContactsListView.as_view(), name='contacts'),
]


# urlpatterns = [
#     path('', views.home, name='home'),
#     path('contacts/', views.contacts, name='contacts'),
#     path('product_detail/<int:product_id>', views.product_detail, name='product_detail'),
# ]