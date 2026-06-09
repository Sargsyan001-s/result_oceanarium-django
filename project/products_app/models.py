from django.db import models

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
