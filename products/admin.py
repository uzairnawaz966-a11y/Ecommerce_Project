from django.contrib import admin
from products.models import (
    Category,
    Brand,
    Product,
    Specification,
    Slider,
    ProductImage,
    ProductComponent,
)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = [
        "id",
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
        "description",
        "created_at",
        "updated_at"
    ]
    prepopulated_fields = {
        "slug": ("name",)
    }


@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "product",
        "image"
    ]


@admin.register(Specification)
class SpecificationAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "product",
        "key",
        "value"
    ]

@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "product",
        "background_image"
    ]

@admin.register(ProductComponent)
class ProductComponentAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "name",
        "product",
        "description",
        "image"
    ]