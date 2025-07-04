from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, ListView, DetailView

from catalog.models import Product


class HomePageView(TemplateView):
    template_name = 'catalog/home.html'


class ContactsPageView(TemplateView):
    template_name = 'catalog/contacts.html'


class ProductListView(ListView):
    model = Product
    template_name = 'products_list.html'
    context_object_name = 'products'


class ProductDetailView(DetailView):
    model = Product
    template_name = 'products_detail.html'
    context_object_name = 'product'


# def home(request):
#     return render(request, 'catalog/home.html')
#
# def contacts(request):
#     return render(request, 'catalog/contacts.html')
#
#
# def products_list(request):
#     products = Product.objects.all()
#     context = {"products": products}
#     return render(request, 'products_list.html', context)
#
# def products_detail(request, pk):
#     product = get_object_or_404(Product, pk=pk)
#     context = {"product": product}
#     return render(request, 'products_detail.html', context)

