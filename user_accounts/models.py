from django.db import models
from django.contrib.auth.models import User
from products.models import Product
# from django.contrib.auth.models import AbstractBaseUser, BaseUserManager



# User Profile related to an Authenticated User_______________
class Profile(models.Model):
    GENDER_CHOICES = [
        ("male", "Male"),
        ("female", "Female"),
        ("other", "Other")
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    phone = models.CharField(max_length=20, null=True, blank=True)
    profile_picture = models.ImageField(upload_to='profile_image/', null=True, blank=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    date_of_birth = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.user.username


# Address of an Authenticated User_______________
class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="addresses")
    company_name = models.CharField(max_length=100, blank=True)
    area_code = models.CharField(max_length=100)
    primary_phone = models.CharField(max_length=15)
    street_address = models.CharField(max_length=255)
    zip_code = models.CharField(max_length=50)
    bussiness_address = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "Addresses"

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"
    
class RatingAndReview(models.Model):
    RATING_CHOICES = [
        (1, "1 Star"),
        (2, "2 Star"),
        (3, "3 Star"),
        (4, "4 Star"),
        (5, "5 Star"),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reviews")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="reviews")
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=255)
    review = models.TextField()
    rating = models.IntegerField(choices=RATING_CHOICES)
    date_and_time = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("user", "product")



# class CustomUserManager(BaseUserManager):

#     def create_user(self, email, password, **extra_fields):
#         if not email:
#             raise ValueError("Email Field is required!")
#         if not password:
#             raise ValueError("Any password for user is compulsory for Login")
        
#         email = self.normalize_email(email)
#         user = self.model(email=email, **extra_fields)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user
    
#     def create_superuser(self, email, password, **extra_fields):
#         if not email:
#             raise ValueError("Email is required!")
#         if not password:
#             raise ValueError("Any password is compulsory for Login")
#         email = self.normalize_email(email)
#         user = self.model(email=email)