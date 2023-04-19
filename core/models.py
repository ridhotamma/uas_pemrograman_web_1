from django.db import models
from django.utils import timezone

# Create your models here.
class Type(models.Model):
    name = models.CharField(max_length=150)
    code = models.CharField(max_length=10)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "types"

    def __str__(self):
        return f'{self.name} - {self.code}'


class Size(models.Model):
    name = models.CharField(max_length=50)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "sizes"

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name
    
class Product(models.Model):
    code = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    categories = models.ManyToManyField(Category)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    size = models.ForeignKey(Size, on_delete=models.CASCADE)
    price = models.FloatField()
    stock_quantity = models.IntegerField()

    class Meta:
        verbose_name_plural = "products"

    def __str__(self):
        return f'{self.name} - {self.code}'


class Sales(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    product_quantity = models.IntegerField()
    date_sold = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "sales"

    def __str__(self):
        return f"{self.product.code} sold on {self.date_sold}"
