from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, ListView, DetailView
from catalog.models import Product

from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Product
from .forms import ProductForm


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

class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'product_form.html'
    success_url = reverse_lazy('catalog:products_list')

class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'product_form.html'
    success_url = reverse_lazy('catalog:products_list')

class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'product_confirm_delete.html'
    success_url = reverse_lazy('catalog:products_list')




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

