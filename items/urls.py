from django.urls import path, include
from .views import home, display_category

urlpatterns = [
    path('', home, name='home'),
    path('category/',display_category, name='display_category'),
]