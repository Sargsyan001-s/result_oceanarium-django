from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(Collection)
class CollectionAdmin(admin.ModelAdmin):
    pass

@admin.register(Aquarium)
class AquariumAdmin(admin.ModelAdmin):
    pass

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass

@admin.register(Inhabitant)
class InhabitantAdmin(admin.ModelAdmin):
    pass

@admin.register(ScheduleEvent)
class ScheduleEventAdmin(admin.ModelAdmin):
    pass

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    pass

@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    pass

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['pk', 'user', 'buyer_surname', 'price', 'date_create', 'delivery_type']

@admin.register(Pos_order)
class Pos_orderAdmin(admin.ModelAdmin):
    list_display = ['pk', 'order', 'product', 'count', 'discount']
