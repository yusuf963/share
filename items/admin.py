from django.contrib import admin
from .models import Item, Category

class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'item_state', 'owner', 'rate')
    list_display_links = ('name', 'category', 'item_state', 'owner', 'rate')
    list_filter = ('category','name', 'item_state', 'owner')
    search_fields = ('name', 'category__name')
    list_per_page = 25

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'color_tag')
    list_display_links = ('name', 'description', 'color_tag')
    list_filter = ('name', 'description', 'color_tag')
    search_fields = ('name', 'description', 'color_tag')
    list_per_page = 25

admin.site.register(Item, ItemAdmin)
admin.site.register(Category, CategoryAdmin)