from django import forms
from .models import Category, Product, Inhabitant, Aquarium, ScheduleEvent
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'description']

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'size', 'color', 'photo', 'is_exists', 'category', 'collection']

class InhabitantForm(forms.ModelForm):
    class Meta:
        model = Inhabitant
        fields = ['name', 'description', 'weight', 'habitat', 'photo', 'is_exists', 'category', 'collection', 'aquarium']

class AquariumForm(forms.ModelForm):
    class Meta:
        model = Aquarium
        fields = ['name', 'description', 'volume', 'depth', 'water_type', 'photo', 'is_exists', 'category', 'collection']

class ScheduleEventForm(forms.ModelForm):
    class Meta:
        model = ScheduleEvent
        fields = ['name', 'description', 'event_time', 'location', 'photo', 'is_exists', 'category', 'collection']

class RegistrationForm(UserCreationForm):
    username = forms.CharField(
        label='Логин пользователя',
        widget=forms.TextInput(attrs={'class':'form-control',}),
        min_length=2
    )
    email = forms.CharField(
        label='электронная почта',
        widget=forms.EmailInput(attrs={'class':'form-control',}),
    )
    password1 = forms.CharField(
        label='Придумайте пароль',
        widget=forms.PasswordInput(attrs={'class':'form-control',}),
    )
    password2 = forms.CharField(
        label='Повторите пароль',
        widget=forms.PasswordInput(attrs={'class':'form-control',}),
    )

class Meta:
    model = User
    fields = ['username','email','password1','password2']

class LoginForm(AuthenticationForm):
    username = forms.CharField(
        label='Логин пользователя',
        widget=forms.TextInput(attrs={'class':'form-control',}),
        min_length=2
    )
    password = forms.CharField(
        label='Введите пароль',
        widget=forms.PasswordInput(attrs={'class':'form-control',}),
    )