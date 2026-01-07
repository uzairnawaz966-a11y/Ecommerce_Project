from products.models import Product, Brand, Category


def categories(request):
    categories = Category.objects.all()
    return {"categories": categories}


def brands(request):
    category = Category.objects.get(name="Mobile Phone")
    brands = Brand.objects.filter(category=category)[:4]
    
    specific_brands = {}
    for brand in brands:
        products = Product.objects.filter(brand=brand, availability="in stock")[:5]
        specific_brands[brand] = products
    
    print(specific_brands)
    return {"specific_brands": specific_brands}

# brands = ["smasung", "iphone", "microsofy", "micromax"]
