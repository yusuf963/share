from django.contrib import admin
from .models import Contract

admin.site.site_header = 'Share Administration Panel'
admin.site.register(Contract)
