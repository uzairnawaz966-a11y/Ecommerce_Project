from django.db import models
from django.contrib.auth.models import User



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
    
class Review(models.Model):
    RATING_CHOICES = [
        (1, "1 Star"),
        (2, "2 Star"),
        (3, "3 Star"),
        (4, "4 Star"),
        (5, "5 Star"),
    ]
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=255)
    review = models.TextField()
    image = models.ForeignKey(Profile, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=RATING_CHOICES)
    date_and_time = models.DateTimeField(auto_now_add=True)