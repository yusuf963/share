from django.contrib import admin
from .models import BlogPost
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title','code', 'author', 'publish_date')  
    list_display_links = ('title', 'author', 'publish_date')
    list_filter = ('title', 'author', 'publish_date')
    search_fields = ('title', 'author', 'publish_date')
    list_per_page = 25

admin.site.register(BlogPost, BlogPostAdmin)
