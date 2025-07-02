# from . import views
# from catalog.apps import CatalogConfig
from django.urls import path
from catalog.views import HomePageView, ContactsPageView, ProductListView, ProductDetailView

app_name = 'products'


urlpatterns = [
    path('home/', HomePageView.as_view(), name='home'),
    path('contacts/', ContactsPageView.as_view(), name='contacts'),
    path('products/', ProductListView.as_view(), name='products_list'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='products_detail'),
]
    # path('home/', views.home, name='home'),
    # path('contacts/', views.contacts, name='contacts'),
    # path('', views.products_list, name='products_list'),
    # path('products/<int:pk>/', views.products_detail, name='products_detail')
#]