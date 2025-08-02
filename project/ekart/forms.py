from django import forms
from django.contrib.auth.models import User
from ekart.models import Cart



class SignUpForm(forms.ModelForm):
    class Meta:
        model= User
        fields=['username','email','password']
        widgets={
            'username':forms.TextInput(attrs={'class':'form-control','placeholder':'usrename'}),
            'email':forms.EmailInput(attrs={'class':'form-control','placeholder':'email'}),
            'password':forms.PasswordInput(attrs={'class':'form-control','placeholder':'password'}),
        }
        
class SignInForm(forms.ModelForm):
    class Meta:
        model= User
        fields=['username','password']
        widgets={
            'username':forms.TextInput(attrs={'class':'form-control','placeholder':'usrename'}),
            'password':forms.PasswordInput(attrs={'class':'form-control','placeholder':'password'}),
        }        
        
        
class CartForm(forms.ModelForm):
    class Meta:
        model=Cart        