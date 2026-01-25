from django.db import models
from decimal import Decimal


# Category_______________
class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


def get_default_category():
    category, created = Category.objects.get_or_create(name="uncategorized")
    return category


# Brand_______________
class Brand(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_DEFAULT, default=get_default_category, related_name="brands")
    brand_name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='brands/', null=True, blank=True)
    slug = models.SlugField()

    def __str__(self):
        return f"{self.brand_name} ( {self.category.name} )"


def get_default_subcategory():
    category, created = Brand.objects.get_or_create(brand_name="No Brand")
    return category


# Products of Brands_______________
class Product(models.Model):
    AVAILABILITY_CHOICES = [
        ("in stock", "In Stock"),
        ("out of stock", "Out of Stock")
    ]
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    brand = models.ForeignKey(Brand, on_delete=models.SET_DEFAULT, default=get_default_subcategory, related_name="products")
    image = models.ImageField(upload_to="product_main_image/")
    description = models.TextField(default="No Description")
    discount = models.PositiveIntegerField(default=0)
    availability = models.CharField(max_length=15, choices=AVAILABILITY_CHOICES, default="in stock")
    slug = models.SlugField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def discounted_price(self):
        if self.discount and self.discount > 0:
            discounted_amount = (self.price * self.discount) / Decimal("100")
            return self.price - discounted_amount
        return self.price
    
    def __str__(self):
        return f"{self.name} ( {self.brand.brand_name} )"


# Slider Images Handler_______________
class Slider(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    background_image = models.ImageField(upload_to="slider_images/")    

    def __str__(self):
        return self.product.name

# Product Specifications_______________
class Specification(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="specifications")
    key = models.CharField(max_length=255)
    value = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.product.name}'s specifications"


# Product Images_______________
class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to="product_gallery/")

    def __str__(self):
        return f"{self.product.name}'s image"
    

class ProductComponent(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="components")
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to="product_components/")

    def __str__(self):
        return f"{self.name} ( {self.product.name} )"