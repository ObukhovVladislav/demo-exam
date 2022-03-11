from django.db import models


class Category(models.Model):
    name = models.CharField('Название', max_length=60)
    desc = models.TextField('Описание', blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    name = models.CharField('Название', max_length=60)
    desc = models.TextField('Описание', blank=True)
    photo = models.ImageField('Фото', upload_to='images/products/', blank=True)
    # product_model = models.CharField('Модель', max_length=30)
    country = models.CharField('Страна-Производитель', max_length=30)
    year = models.IntegerField('Год выпуска')
    price = models.DecimalField('Цена', max_digits=6, decimal_places=2, default=0)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
