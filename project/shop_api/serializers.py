from rest_framework import serializers
from products_app.models import *

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            "name",
            "description"
        ]


class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = [
            "name",
            "description"
        ]


class AquariumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aquarium
        fields = [
            "name",
            "description",
            "volume",
            "depth",
            "water_type",
            "photo",
            "create_date",
            "is_exists",
            "category",
            "collection"
        ]


class ProductSerializer(serializers.ModelSerializer):
    price = serializers.DecimalField(label="Цена", max_digits=20, decimal_places=2)
    class Meta:
        model = Product
        fields = [
            "name",
            "description",
            "price",
            "size",
            "color",
            "photo",
            "create_date",
            "is_exists",
            "category",
            "collection"
        ]

class InhabitantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inhabitant
        fields = [
            "name",
            "description",
            "weight",
            "habitat",
            "photo",
            "create_date",
            "is_exists",
            "category",
            "collection",
            "aquarium"
        ]


class ScheduleEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScheduleEvent
        fields = [
            "name",
            "description",
            "event_time",
            "location",
            "photo",
            "create_date",
            "is_exists",
            "category",
            "collection"
        ]


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = [
            "name",
            "description",
            "position",
            "phone",
            "photo",
            "create_date",
            "is_exists",
            "category",
            "collection"
        ]


class TicketSerializer(serializers.ModelSerializer):
    price = serializers.DecimalField(label="Цена", max_digits=20, decimal_places=2)
    class Meta:
        model = Ticket
        fields = [
            "name",
            "description",
            "price",
            "duration",
            "ticket_type",
            "photo",
            "create_date",
            "is_exists",
            "category",
            "collection"
        ]