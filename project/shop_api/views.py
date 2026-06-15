from django.shortcuts import render
from .serializers import *
from rest_framework import viewsets
from products_app.models import *
from .permission import *
# Create your views here.

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [CustomPermissions]
    pagination_class = PaginationPage
    filter_backends = SearchBackends
    search_fields = ['name', 'description']
    
class CollectionViewSet(viewsets.ModelViewSet):
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer
    permission_classes = [CustomPermissions]
    pagination_class = PaginationPage
    filter_backends = SearchBackends
    search_fields = ['name', 'description']

class AquariumViewSet(viewsets.ModelViewSet):
    queryset = Aquarium.objects.all()
    serializer_class = AquariumSerializer
    permission_classes = [CustomPermissions]
    pagination_class = PaginationPage
    filter_backends = SearchBackends
    search_fields = ['name', 'description', 'water_type']

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [CustomPermissions]
    pagination_class = PaginationPage
    filter_backends = SearchBackends
    search_fields = ['name', 'description', 'color']

class InhabitantViewSet(viewsets.ModelViewSet):
    queryset = Inhabitant.objects.all()
    serializer_class = InhabitantSerializer
    permission_classes = [CustomPermissions]
    pagination_class = PaginationPage
    filter_backends = SearchBackends
    search_fields = ['name', 'description', 'habitat']

class ScheduleEventViewSet(viewsets.ModelViewSet):
    queryset = ScheduleEvent.objects.all()
    serializer_class = ScheduleEventSerializer
    permission_classes = [CustomPermissions]
    pagination_class = PaginationPage
    filter_backends = SearchBackends
    search_fields = ['name', 'description', 'location']

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [CustomPermissions]
    pagination_class = PaginationPage
    filter_backends = SearchBackends
    search_fields = ['name', 'description', 'position', 'phone']

class TicketViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    permission_classes = [CustomPermissions]
    pagination_class = PaginationPage
    filter_backends = SearchBackends
    search_fields = ['name', 'description', 'ticket_type']