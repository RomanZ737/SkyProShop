from django.urls import path
from . import views
from catalog.apps import CatalogConfig
from .views import (
    ProductListView,
    ProductDetailView,
    ContactsListView,
    ProductCreateView,
    ProductUpdateView,
    ProductDeleteView,
    PublishProductView,
    ProductByCategoryView
)

app_name = CatalogConfig.name


urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('product/create/', ProductCreateView.as_view(), name='product_create'),
    path('product/<int:pk>/update/', ProductUpdateView.as_view(), name='product_update'),
    path('product/<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),
    path('contacts/', ContactsListView.as_view(), name='contacts'),
    path('product/<int:pk>/publish/', PublishProductView.as_view(), name='publish_product'),
    path('product/<int:pk>/product_by_category/', ProductByCategoryView.as_view(), name='product_by_category'),
]


# urlpatterns = [
#     path('', views.home, name='home'),
#     path('contacts/', views.contacts, name='contacts'),
#     path('product_detail/<int:product_id>', views.product_detail, name='product_detail'),
# ]