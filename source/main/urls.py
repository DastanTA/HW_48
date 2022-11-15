from django.contrib import admin
from django.urls import path
from ebay.views import main_page, view_product, create_product, update_product, delete_product, by_category_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_page, name='main'),
    path('add/', create_product, name='create_product'),
    path('item/<int:pk>', view_product, name='view_product'),
    path('item/<int:pk>/update', update_product, name='update_product'),
    path('item/<int:pk>/delete', delete_product, name='delete_product'),
    path('<str:category>/', by_category_view, name='by_category'),
]
