from django.shortcuts import render
from django.views.generic import ListView, DetailView

from product.models import Product


class ProductListView(ListView):
    model = Product
    template_name = 'product/products.html'
    paginate_by = 3


class ProductDetailView(DetailView):
    context_object_name = 'product'
    model = Product
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    template_name = 'product/product_detail.html'

# Create your views here.
