from .models import Post,Business
from django.forms import fields
from django import forms

class BusinessForms(forms.ModelForm):
    email=forms.EmailField()
    class Meta:
        model=Business
        fields= ['name','email','business_image','location']

class PostForms(forms.ModelForm):
    class Post:
        fields=['post']