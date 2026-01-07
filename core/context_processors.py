from products.models import Product, Brand, Category


def Brands(request):

    categories = Category.objects.all()
    mobile_phones = Category.objects.get(name="Mobile Phone")

    brands = Brand.objects.filter(category=mobile_phones)[:4]
    brands_with_images = Brand.objects.filter(category__name="Mobile Phone").exclude(image__isnull=True).exclude(image='')

    specific_brands = {}

    for brand in brands:
        specific_brands[brand] = Product.objects.filter(brand=brand, availability="in stock").only("name", "slug")[:5]
    
    return {"Mobile_Phone": specific_brands, "categories": categories, "brand_with_images": brands_with_images}