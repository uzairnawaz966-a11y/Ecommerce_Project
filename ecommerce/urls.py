from django.urls import path
from ecommerce.views import (
    about_us,
    checkout_cart,
    checkout_complete,
    checkout_info,
    checkout_payment,
    contact_us,
    faq,
    my_account,
    product,
    search_results,
)


urlpatterns = [
    path('about_us/', about_us, name="about_us"),
    path('checkout_cart/', checkout_cart, name="checkout_cart"),
    path('checkout_complete/', checkout_complete, name="checkout_complete"),
    path('checkout_info/', checkout_info, name="checkout_info"),
    path('checkout_payment/', checkout_payment, name="checkout_payment"),
    path('contact_us/', contact_us, name="contact_us"),
    path('faq/', faq, name="faq"),
    path('my_account/', my_account, name="my_account"),
    path('product/', product, name="product"),
    path('search_results/', search_results, name="search_results"),
]