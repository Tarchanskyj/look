from django.conf.urls import url
from product import views

app_name = 'product'
urlpatterns = [
    url(r'^$', views.ProductListView.as_view(), name='products_list'),
    url(r'^(?P<slug>[\w-]+)$', views.ProductDetailView.as_view(), name='product_detail')
]
