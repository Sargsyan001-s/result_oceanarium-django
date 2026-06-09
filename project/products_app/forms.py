from django import forms
from .models import Category, Product, Inhabitant, Aquarium, ScheduleEvent

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
