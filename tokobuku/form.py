from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Contacts, Review

class ContactsForm(forms.ModelForm):
    class Meta: 
        model = Contacts
        fields = ['ContactName', 'ContactEmail', 'Message']

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['product_id', 'cust_name', 'cust_email', 'cust_review', 'rate']

class SignupForm(UserCreationForm):
    class Meta:
        model = User 
        fields = ['username', 'password1', 'password2']

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)