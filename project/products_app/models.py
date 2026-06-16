from django.db import models
from django.contrib.auth.models import User

MAX_LENGTH = 255

class Category(models.Model):
    name = models.CharField(max_length=MAX_LENGTH, verbose_name='Наименование')
    description = models.TextField(null=True, blank=True, verbose_name='Описание')
   
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Collection(models.Model):
    name = models.CharField(max_length=MAX_LENGTH, verbose_name='Наименование')
    description = models.TextField(null=True, blank=True, verbose_name='Описание')
   
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Зона'
        verbose_name_plural = 'Зоны'


class Aquarium(models.Model):
    name = models.CharField(max_length=MAX_LENGTH, verbose_name='Наименование')
    description = models.TextField(null=True, blank=True, verbose_name='Описание')
    volume = models.FloatField(verbose_name='Объём (л)')
    depth = models.PositiveIntegerField(default=5, verbose_name='Глубина (м)')
    water_type = models.CharField(max_length=MAX_LENGTH, verbose_name='Тип воды')
    photo = models.ImageField(upload_to='image/%Y/%m/%d', null=True, blank=True, verbose_name='Изображение')
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления на сайт')
    is_exists = models.BooleanField(default=True, verbose_name='Открыт для посещения')

    category = models.ForeignKey(Category, on_delete=models.PROTECT,verbose_name='Категория')
    collection = models.ManyToManyField(Collection, verbose_name='Зона')

    def __str__(self):
        return f"{self.name} ({self.volume} л)"
    
    class Meta:
        verbose_name = 'Аквариум'
        verbose_name_plural = 'Аквариумы'


class Product(models.Model):
    name = models.CharField(max_length=MAX_LENGTH, verbose_name='Наименование')
    description = models.TextField(null=True, blank=True, verbose_name='Описание')
    price = models.FloatField(verbose_name='Цена')
    size = models.PositiveIntegerField(default=1, verbose_name='Количество')
    color = models.CharField(max_length=MAX_LENGTH, verbose_name='Цвет')
    photo = models.ImageField(upload_to='image/%Y/%m/%d', null=True, blank=True, verbose_name='Изображение')
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления на сайт')
    is_exists = models.BooleanField(default=True, verbose_name='Доступность к заказу')

    category = models.ForeignKey(Category, on_delete=models.PROTECT,verbose_name='Категория')
    collection = models.ManyToManyField(Collection, verbose_name='Зона')

    def __str__(self):
        return f"{self.name} ({self.price} руб.)"
    
    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class Inhabitant(models.Model):
    name = models.CharField(max_length=MAX_LENGTH, verbose_name='Наименование')
    description = models.TextField(null=True, blank=True, verbose_name='Описание')
    weight = models.PositiveIntegerField(default=100, verbose_name='Вес (кг)')
    habitat = models.CharField(max_length=MAX_LENGTH, verbose_name='Среда обитания')
    photo = models.ImageField(upload_to='image/%Y/%m/%d', null=True, blank=True, verbose_name='Изображение')
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления на сайт')
    is_exists = models.BooleanField(default=True, verbose_name='На выставке')

    category = models.ForeignKey(Category, on_delete=models.PROTECT,verbose_name='Категория')
    collection = models.ManyToManyField(Collection, verbose_name='Зона')
    aquarium = models.ForeignKey(Aquarium, on_delete=models.PROTECT, verbose_name='Аквариум')

    def __str__(self):
        return f"{self.name} ({self.habitat})"
    
    class Meta:
        verbose_name = 'Обитатель'
        verbose_name_plural = 'Обитатели'


class ScheduleEvent(models.Model):
    name = models.CharField(max_length=MAX_LENGTH, verbose_name='Наименование')
    description = models.TextField(null=True, blank=True, verbose_name='Описание')
    event_time = models.TimeField(verbose_name='Время')
    location = models.CharField(max_length=MAX_LENGTH, verbose_name='Место')
    photo = models.ImageField(upload_to='image/%Y/%m/%d', null=True, blank=True, verbose_name='Изображение')
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления на сайт')
    is_exists = models.BooleanField(default=True, verbose_name='Активно')

    category = models.ForeignKey(Category, on_delete=models.PROTECT,verbose_name='Категория')
    collection = models.ManyToManyField(Collection, verbose_name='Зона')

    def __str__(self):
        return f"{self.name} ({self.event_time})"
    
    class Meta:
        verbose_name = 'Событие'
        verbose_name_plural = 'Расписание'


class Employee(models.Model):
    name = models.CharField(max_length=MAX_LENGTH, verbose_name='Наименование')
    description = models.TextField(null=True, blank=True, verbose_name='Описание')
    position = models.CharField(max_length=MAX_LENGTH, verbose_name='Должность')
    phone = models.CharField(max_length=MAX_LENGTH, verbose_name='Телефон')
    photo = models.ImageField(upload_to='image/%Y/%m/%d', null=True, blank=True, verbose_name='Изображение')
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления на сайт')
    is_exists = models.BooleanField(default=True, verbose_name='Работает')

    category = models.ForeignKey(Category, on_delete=models.PROTECT,verbose_name='Категория')
    collection = models.ManyToManyField(Collection, verbose_name='Зона')

    def __str__(self):
        return f"{self.name} ({self.position})"
    
    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'


class Ticket(models.Model):
    name = models.CharField(max_length=MAX_LENGTH, verbose_name='Наименование')
    description = models.TextField(null=True, blank=True, verbose_name='Описание')
    price = models.FloatField(verbose_name='Цена')
    duration = models.PositiveIntegerField(default=1, verbose_name='Длительность (ч)')
    ticket_type = models.CharField(max_length=MAX_LENGTH, verbose_name='Тип билета')
    photo = models.ImageField(upload_to='image/%Y/%m/%d', null=True, blank=True, verbose_name='Изображение')
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления на сайт')
    is_exists = models.BooleanField(default=True, verbose_name='Доступен к продаже')

    category = models.ForeignKey(Category, on_delete=models.PROTECT,verbose_name='Категория')
    collection = models.ManyToManyField(Collection, verbose_name='Зона')

    def __str__(self):
        return f"{self.name} ({self.price} руб.)"
    
    class Meta:
        verbose_name = 'Билет'
        verbose_name_plural = 'Билеты'


class Order(models.Model):
    SHOP = "SH"
    COURIER = "CR"
    PICKUPPOINT = "PP"

    TYPE_DELIVERY = [
        (SHOP, "Выдача в сувенирной лавке"),
        (COURIER, "Курьер"),
        (PICKUPPOINT, "Пункт выдачи"),
    ]

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Пользователь',
        related_name='orders'
    )
    buyer_firstname = models.CharField(max_length=MAX_LENGTH, verbose_name='Имя')
    buyer_name = models.CharField(max_length=MAX_LENGTH, verbose_name='Отчество', null=True, blank=True)
    buyer_surname = models.CharField(max_length=MAX_LENGTH, verbose_name='Фамилия')
    comment = models.CharField(max_length=MAX_LENGTH, verbose_name='Комментарий', null=True, blank=True)
    delivery_address = models.CharField(max_length=MAX_LENGTH, verbose_name='Адрес доставки')
    delivery_type = models.CharField(max_length=2, choices=TYPE_DELIVERY, verbose_name='Способ получения')
    price = models.FloatField(default=0, verbose_name='Сумма заказа')
    date_create = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    date_finish = models.DateTimeField(null=True, blank=True, verbose_name='Дата завершения')

    product = models.ManyToManyField(Product, through='Pos_order', verbose_name='Сувениры')

    def __str__(self):
        return f"#{self.pk} - {self.buyer_surname} {self.buyer_firstname} ({self.date_create})"

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'


class Pos_order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Сувенир')
    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name='Заказ')
    count = models.PositiveIntegerField(default=1, verbose_name='Количество')
    discount = models.PositiveIntegerField(default=0, verbose_name='Скидка')

    def __str__(self):
        return f"Заказ #{self.order_id} - {self.product.name}"

    class Meta:
        verbose_name = 'Позиция заказа'
        verbose_name_plural = 'Позиции заказов'
