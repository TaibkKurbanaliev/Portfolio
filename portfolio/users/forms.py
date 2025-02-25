from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm

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
        
class UserProfileForm(UserChangeForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs= {
            'class': 'form-control',
            'placeholder': 'First name'
        }), max_length=150, required=True)
    second_name = forms.CharField(widget=forms.TextInput(attrs= {
            'class': 'form-control',
            'placeholder': 'Second name'
        }), max_length=150, required=True)
    username = forms.CharField(widget=forms.TextInput(attrs= {
            'class': 'form-control readonly-field',
            'placeholder': 'Username',
            'readonly': True
        }), required=False)
    email = forms.CharField(widget=forms.EmailInput(attrs= {
            'class': 'form-control readonly-field',
            'placeholder': 'Email',
            'readonly': True
        }), required=False)
    image = forms.ImageField(widget=forms.FileInput(attrs= {
            'class': 'custom-file-input',
            'placeholder': 'Image',
            'id': 'uploadImage',
            'style': 'display: none;'
        }), required=False)
    website = forms.CharField(widget=forms.URLInput(attrs= {
            'class': 'form-control',
            'placeholder': 'Website'
        }), max_length=128, required=False)
    telegram = forms.CharField(widget=forms.URLInput(attrs= {
            'class': 'form-control',
            'placeholder': 'Telegram'
        }), max_length=64, required=False)
    github = forms.CharField(widget=forms.URLInput(attrs= {
            'class': 'form-control',
            'placeholder': 'Github'
        }), max_length=256, required=False)
    phone = forms.CharField(widget=forms.NumberInput(attrs= {
            'class': 'form-control',
            'placeholder': 'Phone number'
        }), max_length=20, required=False)
    city = forms.CharField(widget=forms.TextInput(attrs= {
            'class': 'form-control',
            'placeholder': 'City'
        }), max_length=128, required=False)
    class Meta:
        model = User
        fields = ('first_name', 'second_name', 'image', 'email', 'username', 'city', 'phone',  'website', 'telegram', 'github')