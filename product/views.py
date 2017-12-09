from django.shortcuts import reverse
from django.contrib import messages
from django.views.generic import ListView, DetailView, FormView
from django.views.generic.detail import SingleObjectMixin


from product.models import Product, Comment
from product.forms import CommentModelForm

import datetime


class ProductListView(ListView):
    model = Product
    template_name = 'product/products.html'
    paginate_by = 3


class ProductDetailView(SingleObjectMixin, FormView):
    form_class = CommentModelForm
    context_object_name = 'product'
    model = Product
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    template_name = 'product/product_detail.html'

    def get_context_data(self, **kwargs):
        context = super(ProductDetailView, self).get_context_data(**kwargs)
        date_from = datetime.datetime.now() - datetime.timedelta(days=1)
        context['comments'] = Comment.objects.filter(product=self.object, created_at__gte=date_from)
        return context

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super(ProductDetailView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        '''Add new Comment'''
        form = self.get_form()
        if form.is_valid():
            author = form.cleaned_data['author']
            text = form.cleaned_data['text']
            Comment.objects.create(author=author, text=text, product=self.get_object())
            messages.success(self.request, 'Comment was added successfully!')
        else:
            messages.warning(request, 'Please correct the error below.')
            return self.form_invalid(form)
        return super(ProductDetailView, self).post(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('product:product_detail', kwargs={'slug': self.kwargs['slug']})

# Create your views here.
