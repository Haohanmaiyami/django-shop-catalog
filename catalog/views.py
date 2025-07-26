from django.contrib.auth.decorators import permission_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView
from catalog.models import Product
from django.http import HttpResponseForbidden
from django.shortcuts import get_object_or_404, redirect, render

from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Product
from .forms import ProductForm
from .services import get_products_from_cache, get_products_by_category
from catalog.models import Category


class HomePageView(TemplateView):
    template_name = 'catalog/home.html'


class ContactsPageView(TemplateView):
    template_name = 'catalog/contacts.html'


class ProductListView(ListView):
    model = Product
    template_name = 'products_list.html'
    context_object_name = 'products'



    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated and (user.is_superuser or user.groups.filter(name='Модератор продуктов').exists()):
            return Product.objects.all()
        return get_products_from_cache()


class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product
    template_name = 'products_detail.html'
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        context['is_moderator'] = user.groups.filter(name="Модератор продуктов").exists()
        return context

class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'product_form.html'
    success_url = reverse_lazy('catalog:products_list')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'product_form.html'
    success_url = reverse_lazy('catalog:products_list')

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.owner != request.user and not request.user.is_superuser:
            return HttpResponseForbidden("Вы не являетесь владельцем этого продукта.")
        return super().dispatch(request, *args, **kwargs)


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    template_name = 'product_confirm_delete.html'
    success_url = reverse_lazy('catalog:products_list')

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if (
            obj.owner != request.user
            and not request.user.groups.filter(name='Модератор продуктов').exists()
            and not request.user.is_superuser
        ):
            return HttpResponseForbidden("Удаление доступно только владельцу, модератору или администратору.")
        return super().dispatch(request, *args, **kwargs)


@permission_required('catalog.can_unpublish_product')
def unpublish_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    product.is_active = False
    product.save()
    return redirect('products:products_list')

class ProductsByCategoryView(View):
    def get(self, request, category_id):
        category = get_object_or_404(Category, pk=category_id)
        products = get_products_by_category(category_id)
        return render(request, "catalog/products_by_category.html", {
            "products": products,
            "category": category,
        })

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

