from django.urls import path, include
from rest_framework import routers
from . import views
from . import viewsets

app_name = 'sales'

router = routers.DefaultRouter()
router.register(r'products', viewsets.ProductViewSet, basename='product')
router.register(r'sales', viewsets.SalesViewSet)
router.register(r'types', viewsets.TypeViewSet)
router.register(r'sizes', viewsets.SizeViewSet)
router.register(r'categories', viewsets.CategoryViewSet)
router.register(r'users', viewsets.UserViewSet)

urlpatterns = [
    path('', views.index, name='index'),
    path('add_sale/', views.add_sale, name='add_sale'),
    path('edit_sale/<int:pk>/', views.edit_sale, name='edit_sale'),
    path('delete_sale/<int:pk>/', views.delete_sale, name='delete_sale'),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
]
