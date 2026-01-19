from django.contrib import admin
from products.models import Category, Brand, Product, Image, Specification


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = [
        "name",
    ]


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "brand_name",
        "category",
        "image"
    ]
    prepopulated_fields = {
        "slug": ("brand_name",)
    }


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "name",
        "price",
        "brand",
        "image",
        "discount",
        "created_at",
        "updated_at"
    ]
    prepopulated_fields = {
        "slug": ("name",)
    }


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = [
        "product",
        "image"
    ]


@admin.register(Specification)
class SpecificationAdmin(admin.ModelAdmin):
    list_display = [
        "product",
        "key",
        "value"
    ]