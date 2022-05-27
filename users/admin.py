from django.contrib import admin
from .models import User
admin.site.register(User)

class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'is_superuser')
    list_display_links = ('username', 'email', 'first_name', 'last_name','is_superuser')
    list_filter = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'is_superuser')
    search_fields = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'is_superuser')
    list_per_page = 25