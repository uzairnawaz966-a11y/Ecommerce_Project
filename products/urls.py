from django.urls import path
from products.views import home, ProductDetail


urlpatterns = [
    path('home/', home.as_view(), name="home"),
    path('details/<slug:slug>', ProductDetail.as_view(), name="product_detail"),
]