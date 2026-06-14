from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name='Название категории')
    description = models.TextField(verbose_name='Описание категории')

    def __str__(self):
        return f'{self.name} {self.description}'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['name']


class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name='Название продукта')
    description = models.TextField(verbose_name='Описание продукта')
    image = models.ImageField(upload_to='images/', null=True,
                              default='images/default_product.jpg', verbose_name='Изображение продукта')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория продукта')
    price = models.FloatField(verbose_name='Цена за покупку')
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return f'{self.name} {self.price} {self.category} {self.description}'

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ['name']


class Contacts(models.Model):
    country = models.CharField(max_length=150, verbose_name="Название страны")
    tax_num = models.IntegerField(verbose_name="ИНН")
    address = models.TextField(verbose_name='Адрес')

    def __str__(self):
        return f'{self.country}'

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'
