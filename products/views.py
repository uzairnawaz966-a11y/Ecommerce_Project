from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormMixin
from django.urls import reverse

from products.models import Product, Category, Slider, ProductImage
from user_accounts.forms import RatingAndReviewForm


class HomeView(ListView):
    model = Product
    template_name = "ecommerce/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        trending_items = Product.objects.filter(availability="in stock").order_by("-created_at")[:6]
        context["product_list"] = trending_items

        slider_products = Slider.objects.select_related("product")
        context["slider_products"] = slider_products

        categories = Category.objects.prefetch_related("brands__products__specifications")
        context["categories"] = categories

        promotional_products = Product.objects.all().order_by("-discount")[:5]
        context["big_card"] = promotional_products[0]
        context["small_cards"] = promotional_products[1:]

        tablet_category = Category.objects.get(name="Tablet")
        context["tablets"] = Product.objects.filter(brand__category=tablet_category)[:6]

        return context


class ProductDetailView(FormMixin, DetailView):
    model = Product
    template_name = "ecommerce/product_detail.html"
    context_object_name = "Product_detail"
    form_class = RatingAndReviewForm

    def get_success_url(self):
        return reverse("product_detail", args=[self.object.slug])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        specifics = self.object.specifications.filter(key__in=["Color", "RAM"])
        context["specifics"] = specifics

        if "form" not in context:
            context["form"] = self.get_form()

        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()

        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.product = self.object
            review.save()
            return self.form_valid(form)

        return self.form_invalid(form)
