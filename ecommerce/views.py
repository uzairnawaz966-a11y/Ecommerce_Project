from django.shortcuts import render




def about_us(request):
    return render(request, "ecommerce/about_us.html")

def checkout_cart(request):
    return render(request, "ecommerce/checkout_cart.html")

def checkout_complete(request):
    return render(request, "ecommerce/checkout_complete.html")

def checkout_info(request):
    return render(request, "ecommerce/checkout_info.html")

def checkout_payment(request):
    return render(request, "ecommerce/checkout_payment.html")

def contact_us(request):
    return render(request, "ecommerce/contact_us.html")

def faq(request):
    return render(request, "ecommerce/faq.html")

def my_account(request):
    return render(request, "ecommerce/my_account.html")

def product(request):
    return render(request, "ecommerce/product.html")

def search_results(request):
    return render(request, "ecommerce/search_results.html")