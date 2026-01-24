from django import forms
from user_accounts.models import RatingAndReview


class RatingAndReviewForm(forms.ModelForm):
    class Meta:
        model = RatingAndReview
        fields = ["name", "title", "review", "rating"]