from django.urls import path
from products.views import HomeView, ProductDetailView


urlpatterns = [
    path('home/', HomeView.as_view(), name="home"),
    path('details/<slug:slug>/', ProductDetailView.as_view(), name="product_detail"),
]