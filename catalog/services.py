from .models import Product, Category

class CategoryService:

    @staticmethod
    def get_category_list():
        # Получаем список категорий для выпадающего меню
        categories = Category.objects.all()
        return categories

    @staticmethod
    def get_product_list_by_category(category):
        # получаем список товаров по категории
        products = Product.objects.filter(category=category)
        return products