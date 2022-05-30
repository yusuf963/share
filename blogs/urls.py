from django.urls import URLPattern, path, include
from .views import home
urlpatterns=[
    path('', home, name='home'),
]