# from collections import defaultdict
from products.models import Product, Brand, Category


def Brands(request):

    categories = Category.objects.all()
    
    mobile_phones = Category.objects.filter(name="Mobile Phone").first()
    if not mobile_phones:
        return {"categories": categories}

    brands = Brand.objects.filter(category=mobile_phones)[:4]


    specific_brands = {}

    for brand in brands:
        specific_brands[brand] = Product.objects.filter(brand=brand, availability="in stock").only("name", "slug")[:5]


    brands_with_images = Brand.objects.filter(category__name="Mobile Phone").exclude(image__isnull=True).exclude(image='')
    
    return {
        "Mobile_Phone": specific_brands,
        "categories": categories,
        "brand_with_images": brands_with_images,
        }