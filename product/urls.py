from django.conf.urls import url
from product import views


app_name = 'product'
urlpatterns = [
    url(r'^$', views.MainPage.as_view(), name='main'),
    url(r'^products/$', views.ProductListView.as_view(), name='products_list'),
    url(r'^products/(?P<slug>[\w-]+)$', views.ProductDetailView.as_view(), name='product_detail')
]
