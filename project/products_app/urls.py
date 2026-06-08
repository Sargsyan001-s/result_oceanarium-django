from django.urls import path
from .views import *

urlpatterns = [
    path('info/',info_view, name='info_view'),
]
from django.urls import path
from . import views

urlpatterns = [
    path('info/', views.info_view, name='info'),
    path('about/', views.about_view, name='about'),
    path('contacts/', views.contacts_view, name='contacts'),
    path('location/', views.location_view, name='location'),
    path('products/', views.products_view, name='products'),
    path('categories/', views.categories_view, name='categories'),
    path('cart/', views.cart_view, name='cart'),
    path('inhabitants/', views.inhabitants_view, name='inhabitants'),
    path('schedule/', views.schedule_view, name='schedule'),
]