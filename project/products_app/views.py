from django.shortcuts import render
from django.views.generic import ListView,DeleteView,CreateView,DetailView,UpdateView
from .models import *
from django.urls import reverse_lazy
from .forms import *
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required, permission_required
from django.utils.decorators import method_decorator
from django.shortcuts import redirect

# Create your views here.
def info_view(request):
    return render(request,"aquarium/info.html")


def about_view(request):
    return render(request, "aquarium/about.html")

def contacts_view(request):
    return render(request, "aquarium/contacts.html")

def location_view(request):
    return render(request, "aquarium/location.html")

def cart_view(request):
    return render(request, "aquarium/cart.html")

class CategoryListView(ListView):
    model = Category
    template_name = 'aquarium/categories.html'
    context_object_name = 'category_list'

class CategoryDetailView(DetailView):
    model = Category
    template_name = 'aquarium/categories_detail.html'
    context_object_name = 'category'

@method_decorator(permission_required('products_app.add_category'), name='dispatch')
class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'aquarium/categories_form.html'
    success_url = reverse_lazy('category_list')

@method_decorator(permission_required('products_app.change_category'), name='dispatch')
class CategoryUpdateView(UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = 'aquarium/categories_form.html'
    success_url = reverse_lazy('category_list')

@method_decorator(permission_required('products_app.delete_category'), name='dispatch')
class CategoryDeleteView(DeleteView):
    model = Category
    template_name = 'aquarium/categories_confirm_delete.html'
    success_url = reverse_lazy('category_list')

class ProductListView(ListView):
    model = Product
    template_name = 'aquarium/products.html'
    context_object_name = 'product_list'

class ProductDetailView(DetailView):
    model = Product
    template_name = 'aquarium/products_detail.html'
    context_object_name = 'product'

@method_decorator(permission_required('products_app.add_product'), name='dispatch')
class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'aquarium/products_form.html'
    success_url = reverse_lazy('product_list')

@method_decorator(permission_required('products_app.change_product'), name='dispatch')
class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'aquarium/products_form.html'
    success_url = reverse_lazy('product_list')

@method_decorator(permission_required('products_app.delete_product'), name='dispatch')
class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'aquarium/products_confirm_delete.html'
    success_url = reverse_lazy('product_list')

class InhabitantListView(ListView):
    model = Inhabitant
    template_name = 'aquarium/inhabitants.html'
    context_object_name = 'inhabitant_list'

class InhabitantDetailView(DetailView):
    model = Inhabitant
    template_name = 'aquarium/inhabitants_detail.html'
    context_object_name = 'inhabitant'

@method_decorator(permission_required('products_app.add_inhabitant'), name='dispatch')
class InhabitantCreateView(CreateView):
    model = Inhabitant
    form_class = InhabitantForm
    template_name = 'aquarium/inhabitants_form.html'
    success_url = reverse_lazy('inhabitant_list')

@method_decorator(permission_required('products_app.change_inhabitant'), name='dispatch')
class InhabitantUpdateView(UpdateView):
    model = Inhabitant
    form_class = InhabitantForm
    template_name = 'aquarium/inhabitants_form.html'
    success_url = reverse_lazy('inhabitant_list')

@method_decorator(permission_required('products_app.delete_inhabitant'), name='dispatch')
class InhabitantDeleteView(DeleteView):
    model = Inhabitant
    template_name = 'aquarium/inhabitants_confirm_delete.html'
    success_url = reverse_lazy('inhabitant_list')

class AquariumListView(ListView):
    model = Aquarium
    template_name = 'aquarium/aquarium_list.html'
    context_object_name = 'aquarium_list'

class AquariumDetailView(DetailView):
    model = Aquarium
    template_name = 'aquarium/aquarium_detail.html'
    context_object_name = 'aquarium'

@method_decorator(permission_required('products_app.add_aquarium'), name='dispatch')
class AquariumCreateView(CreateView):
    model = Aquarium
    form_class = AquariumForm
    template_name = 'aquarium/aquarium_form.html'
    success_url = reverse_lazy('aquarium_list')

@method_decorator(permission_required('products_app.change_aquarium'), name='dispatch')
class AquariumUpdateView(UpdateView):
    model = Aquarium
    form_class = AquariumForm
    template_name = 'aquarium/aquarium_form.html'
    success_url = reverse_lazy('aquarium_list')

@method_decorator(permission_required('products_app.delete_aquarium'), name='dispatch')
class AquariumDeleteView(DeleteView):
    model = Aquarium
    template_name = 'aquarium/aquarium_confirm_delete.html'
    success_url = reverse_lazy('aquarium_list')

class ScheduleEventListView(ListView):
    model = ScheduleEvent
    template_name = 'aquarium/schedule.html'
    context_object_name = 'schedule_list'

class ScheduleEventDetailView(DetailView):
    model = ScheduleEvent
    template_name = 'aquarium/schedule_detail.html'
    context_object_name = 'schedule'

@method_decorator(permission_required('products_app.add_scheduleevent'), name='dispatch')
class ScheduleEventCreateView(CreateView):
    model = ScheduleEvent
    form_class = ScheduleEventForm
    template_name = 'aquarium/schedule_form.html'
    success_url = reverse_lazy('schedule_list')

@method_decorator(permission_required('products_app.change_scheduleevent'), name='dispatch')
class ScheduleEventUpdateView(UpdateView):
    model = ScheduleEvent
    form_class = ScheduleEventForm
    template_name = 'aquarium/schedule_form.html'
    success_url = reverse_lazy('schedule_list')

@method_decorator(permission_required('products_app.delete_scheduleevent'), name='dispatch')
class ScheduleEventDeleteView(DeleteView):
    model = ScheduleEvent
    template_name = 'aquarium/schedule_confirm_delete.html'
    success_url = reverse_lazy('schedule_list')

def login_user(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            if request.GET.get('next'):
                return redirect(request.GET.get('next'))
            return redirect('info_view')
    else:
        form = LoginForm()
    context = {
        'form': form
    }
    return render(request, 'auth/login.html', context)

def registration_user(request):
    if request.method == 'POST':
        form = RegistrationForm(data=request.POST)
        if form.is_valid():
            login(request, form.save())
            if request.GET.get('next'):
                return redirect(request.GET.get('next'))
            return redirect('info_view')
    else:
        form = RegistrationForm()
    context = {
        'form': form
    }
    return render(request, 'auth/registration.html', context)

def logout_user(request):
    logout(request)
    return redirect('info_view')