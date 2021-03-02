from salestrackingapp.models import *
from django import forms

class CustomUserCreationForm(forms.Form):
    # username = forms.CharField(label='Enter Username', min_length=4, max_length=150,widget= forms.TextInput(attrs={'class':'form-control'}))
    PhoneNumber = forms.CharField(label='Enter First Name', min_length=4, max_length=150,widget= forms.TextInput(attrs={'class':'form-control'}))
    Age = forms.IntegerField(label='Enter Age', widget= forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(label='Enter email',widget= forms.TextInput(attrs={'class':'form-control'}))
    password1 = forms.CharField(label='Enter password', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput(attrs={'class':'form-control'}))