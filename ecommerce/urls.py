
from django.contrib import admin
from django.urls import path, include
from .router import router

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include((router.urls, 'products'))),
    path('', include((router.urls, 'order'))),
]
