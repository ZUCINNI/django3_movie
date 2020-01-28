from django import forms
from .models import Reviews


class ReviewForm(forms.ModelForm):
    """Form for adding reviews"""

    class Meta:
        model = Reviews
        fields = ("name", "email", "text")
