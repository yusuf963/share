from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User as MyUser  # my Custom User Model
# from django.contrib.auth.models import User
# admin.site.unregister(User)

class UserAdmin(UserAdmin):
    list_display = ('username', 'email')    
    list_display_links = ('username', 'email')
    list_filter = ('username', 'email')
    search_fields = ('username', 'email')
    ordering = ('username', 'email')
    fieldsets = ()
    list_per_page = 25
admin.site.register(MyUser,UserAdmin)