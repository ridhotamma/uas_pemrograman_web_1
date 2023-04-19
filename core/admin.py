from django.contrib import admin
from .models import Sales, Size, Type, Product, Category

# Register your models here.
admin.site.register(Sales)
admin.site.register(Size)
admin.site.register(Type)
admin.site.register(Product)
admin.site.register(Category)
