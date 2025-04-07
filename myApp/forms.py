from django import forms
from .models import Categories,Products,Profile


class CategoryForm(forms.ModelForm):
    class Meta:
        model= Categories
        fields='__all__'

class ProductForm(forms.ModelForm):
    class Meta:
        model= Products
        exclude=['us']
        # fields='__all__'      


class ProfileForm(forms.ModelForm):
    class Meta:
        model= Profile
        exclude=['us']
        # fields='__all__'