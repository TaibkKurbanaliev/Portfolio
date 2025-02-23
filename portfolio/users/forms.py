from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from users.models import User

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs= {
            'class': 'form-control',
            'placeholder': 'Username'
        }), max_length=150, required=True)
    password = forms.CharField(widget=forms.PasswordInput(attrs= {
            'class': 'form-control',
            'placeholder': 'Password'
        }), max_length=64, required=True)
    class Meta:
        model = User
        fields = ('username', 'password')
        
class UserRegistartionForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs= {
            'class': 'form-control',
            'placeholder': 'First name'
        }), max_length=150, required=True)
    second_name = forms.CharField(widget=forms.TextInput(attrs= {
            'class': 'form-control',
            'placeholder': 'Second name'
        }), max_length=150, required=True)
    username = forms.CharField(widget=forms.TextInput(attrs= {
            'class': 'form-control',
            'placeholder': 'Username'
        }), max_length=150, required=True)
    email = forms.CharField(widget=forms.EmailInput(attrs= {
            'class': 'form-control',
            'placeholder': 'Email'
        }), max_length=150, required=True)
    password1 = forms.CharField(widget=forms.PasswordInput(attrs= {
            'class': 'form-control',
            'placeholder': 'password'
        }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs= {
            'class': 'form-control',
            'placeholder': 'confirm'
        }))
    class Meta:
        model = User
        fields = ('first_name', 'second_name', 'email', 'username')