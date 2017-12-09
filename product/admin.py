from django.contrib import admin
from django.urls import reverse

from product.models import Product, Comment, Like


class ProductAdmin(admin.ModelAdmin):

    def view_on_site(self, obj):
        return reverse('product:product_detail', kwargs={'slug': obj.slug})


admin.site.register(Product, ProductAdmin)
admin.site.register(Comment)
admin.site.register(Like)