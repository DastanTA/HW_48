from django.contrib import admin
from django.urls import path
from ebay.views import main_page, view_product

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_page, name='main'),
    path('item/<int:pk>', view_product, name='view_product'),
]
