from django.urls import path, include
from .views import home, display_category,display_items

urlpatterns = [
    path('', home, name='home'),
    path('category/',display_category, name='display_category'),
    path('itempage/',display_items, name='display_category'),
]