from django.shortcuts import reverse
from django.contrib import messages
from django.views.generic import ListView, DetailView, FormView, TemplateView, View, UpdateView
from django.views.generic.detail import SingleObjectMixin
from django.contrib.auth.forms import AuthenticationForm
from django.core.cache import cache

from product.models import Product, Comment, Like
from product.forms import CommentModelForm, LikeModelForm

import datetime
import operator


class MainPage(TemplateView):
    '''Main page'''
    authentication_form = AuthenticationForm
    template_name = 'index.html'


class ProductListView(ListView):
    '''Products page. Queryset for it takes from cache. Cache updates on signal post_save for model Product'''
    login_url = 'login'
    model = Product
    template_name = 'product/products.html'
    paginate_by = 6
    ordering = 'created_at'

    def get_queryset(self, *args, **kwargs):
        queryset = cache.get('queryset')
        if queryset is None:
            queryset = Product.objects.all()
            cache.set('queryset', queryset, 60 * 30)
        ordering = self.get_ordering()
        if ordering:
            if ordering == 'likes_counter':
                queryset = sorted(queryset, key=operator.attrgetter(ordering), reverse=True)
            else:
                queryset = sorted(queryset, key=operator.attrgetter(ordering))
        return queryset

    def get_ordering(self):
        if self.request.GET.get('order') == 'likes':
            self.ordering = 'likes_counter'
        elif self.request.GET.get('order') == 'name':
            self.ordering = 'name'
        return self.ordering


class ProductDetailView(SingleObjectMixin, FormView):
    '''Product page with two forms for Like and Comment'''
    form_class = CommentModelForm
    context_object_name = 'product'
    model = Product
    prefix = 'comment'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    template_name = 'product/product_detail.html'

    def get_context_data(self, **kwargs):
        context = super(ProductDetailView, self).get_context_data(**kwargs)
        date_from = datetime.datetime.now() - datetime.timedelta(days=1)
        context['comments'] = Comment.objects.filter(product=self.object, created_at__gte=date_from)
        context['like_form'] = LikeModelForm(prefix='like', initial={'product': self.get_object(), 'user': self.request.user})
        return context

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super(ProductDetailView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        '''Add new Comment or Like. It check form name from page.'''
        self.object = self.get_object()
        if self.request.POST.get('form_name') == 'comment':
            form_comment = CommentModelForm(self.request.POST, prefix='comment')
            if form_comment.is_valid():
                author = form_comment.cleaned_data['author']
                text = form_comment.cleaned_data['text']
                Comment.objects.create(author=author, text=text, product=self.get_object())
                messages.success(self.request, 'Comment was added successfully!')
            else:
                messages.warning(request, 'Please correct data in comment form.')
                return self.form_invalid(form_comment)

        elif self.request.POST.get('form_name') == 'like':
            form_like = LikeModelForm(self.request.POST, prefix='like')
            if self.request.user.is_authenticated:
                if form_like.is_valid():
                    if Like.objects.filter(product=self.object, user=self.request.user).exists():
                        messages.warning(request, 'Your vote is already exist.')
                    else:
                        form_like.save()
                        self.object.likes_counter += 1
                        self.object.save()
                        messages.success(self.request, 'Thank you for your vote!')
                    return self.form_valid(form_like)
            else:
                messages.warning(request, 'Please login!!!')
                return self.form_valid(form_like)
        return super(ProductDetailView, self).post(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('product:product_detail', kwargs={'slug': self.kwargs['slug']})
