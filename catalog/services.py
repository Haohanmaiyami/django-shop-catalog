from django.core.cache import cache

from catalog.models import Product
from config.settings import CACHE_ENABLED

def get_products_from_cache():
    """Получаем данные по продуктам из кэша, если кэш пуст, получает данные из БД"""
    if not CACHE_ENABLED:
        return Product.objects.all()
    key = "products_list"
    products = cache.get(key)
    if products is not None:
        return products
    products = Product.objects.all()
    cache.set(key, products)
    return products

from catalog.models import Product

def get_products_by_category(category_id):
    """Возвращает активные продукты для указанной категории"""
    return Product.objects.filter(category_id=category_id, is_active=True)
