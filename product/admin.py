from django.contrib import admin
from django.urls import reverse

from product.models import Product


class ProductAdmin(admin.ModelAdmin):

    def view_on_site(self, obj):
        return reverse('product:product_detail',
                                              kwargs={'slug': obj.slug})



admin.site.register(Product, ProductAdmin)