from rest_framework import routers
from eApp import views

router = routers.DefaultRouter()
router.register('products', views.ProductViewset, basename='products')
router.register('order', views.OrderViewset, basename='order')