from django.db import models

from users.models import User


class ProductCategory(models.Model):
    name = models.CharField(max_length=128, unique=True)
    description = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Product(models.Model):
    SIZE_CHOICES = [
        ('XS', 'XS'),
        ('S', 'S'),
        ('M', 'M'),
        ('L', 'L'),
        ('XL', 'XL')
    ]
    name = models.CharField(max_length=128, verbose_name='Название')
    brand = models.CharField(max_length=128, null=True, blank=True, verbose_name='Бренд')
    description = models.TextField(verbose_name='Описание')
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Цена')
    discount = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True, verbose_name='Скидка')
    size = models.CharField(max_length=2, choices=SIZE_CHOICES, null=True, blank=True, verbose_name='Размер')
    quantity = models.PositiveIntegerField(default=0, verbose_name='Количество')
    image_1 = models.ImageField(upload_to='products_images/', verbose_name='1 картинка')
    image_2 = models.ImageField(upload_to='products_images/', null=True, blank=True, verbose_name='2 картинка')
    image_3 = models.ImageField(upload_to='products_images/', null=True, blank=True, verbose_name='3 картинка')
    category = models.ForeignKey(to=ProductCategory, on_delete=models.CASCADE, verbose_name='Категория')

    def discount_price(self):
        if self.discount is not None:
            return self.price - (self.discount / 100) * self.price
        return self.price

    class Meta:
        verbose_name = 'product'
        verbose_name_plural = 'Products'


    def __str__(self):
        return self.name


class Basket(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, verbose_name='Пользователь')
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE, verbose_name='Товар')
    size = models.CharField(max_length=2, choices=Product.SIZE_CHOICES, null=True, blank=True, verbose_name='Размер')
    quantity = models.PositiveSmallIntegerField(default=0, verbose_name='Количество')
    created_timestamp = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    def __str__(self):
        return f'Корзина для {self.user.username} | Продукт: {self.product.name}'
    
    def sum(self):
        return self.product.price * self.quantity
    
    def discount_sum(self):
        discount = self.product.discount
        if discount is not None and discount > 0:
            discounted_price = self.product.price * (1 - discount / 100)
            return discounted_price * self.quantity
        else:
            return self.product.price * self.quantity
    