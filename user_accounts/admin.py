from django.contrib import admin
from user_accounts.models import Profile, Address, RatingAndReview


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


@admin.register(RatingAndReview)
class RatingAndReviewAdmin(admin.ModelAdmin):
    list_display = [
        "user",
        "name",
        "title",
        "review",
        "rating",
        "date_and_time",
    ]