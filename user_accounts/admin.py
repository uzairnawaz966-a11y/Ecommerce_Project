from django.contrib import admin
from django.contrib.auth.models import User
from user_accounts.models import Profile, Address, Review


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = [
        "user",
        "phone",
        "profile_picture",
        "gender",
        "date_of_birth"
    ]


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = [
        "user",
        "company_name",
        "area_code",
        "primary_phone",
        "street_address",
        "zip_code",
        "bussiness_address"
    ]


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "title",
        "review",
        "image",
        "rating",
        "date_and_time"
    ]