from django.shortcuts import render

# Create your views here.
def info_view(request):
    return render(request,"info.html")
from django.shortcuts import render

def about_view(request):
    return render(request, "about.html")

def contacts_view(request):
    return render(request, "contacts.html")

def location_view(request):
    return render(request, "location.html")

def products_view(request):
    return render(request, "products.html")

def categories_view(request):
    return render(request, "categories.html")

def cart_view(request):
    return render(request, "cart.html")

def inhabitants_view(request):
    return render(request, "inhabitants.html")

def schedule_view(request):
    return render(request, "schedule.html")
