from django.views.generic import ListView, DetailView
from products.models import Product, Category



class home(ListView):
    model = Product
    template_name = "ecommerce/index.html"

    # def get_queryset(self):
    #     return Product.objects.select_related(
    #         "brand",
    #         "brand__category"
    #     )
    
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    
    #     categories = Category.objects.filter(name__in=["Mobile Phone", "Tablet"])




    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        trending_items = Product.objects.filter(availability="in stock").order_by("-created_at")[:6] 
        context["product_list"] = trending_items

        Mobile_Phone = Category.objects.get(name="Mobile Phone")
        all_mobile_phones = Product.objects.filter(brand__category=Mobile_Phone)[:6]
        context["mobile_phones"] = all_mobile_phones

        tablets = Category.objects.get(name="Tablet")
        all_tablets = Product.objects.filter(brand__category=tablets)[:6]
        context["tablets"] = all_tablets
        
        return context


class ProductDetail(DetailView):
    model = Product
    template_name = "ecommerce/product_detail.html"