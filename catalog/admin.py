from django.contrib import admin
from .models import Product, Category, Contacts


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (id, 'name', 'price', 'category', 'created_at', 'updated_at')
    list_filter = ('category', 'created_at', 'updated_at')
    search_fields = ('name', 'category', 'description',)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (id, 'name', 'description')
    list_filter = ('name', 'description')
    search_fields = ('name', 'description')

@admin.register(Contacts)
class ContactsAdmin(admin.ModelAdmin):
    list_display = (id, 'country', 'tax_num', 'address')
