from django.contrib import admin
from .models import Contract
class ContractAdmin(admin.ModelAdmin):
    list_display = ('name', 'carbon_emissions_reduced')
    list_display_links = ('name', 'carbon_emissions_reduced', 'item_condition', 'rate')
    list_filter = ('name','carbon_emissions_reduced',)
    search_fields = ('name', 'carbon_emissions_reduced')
    list_per_page = 25

admin.site.site_header = 'Share Administration Panel'
admin.site.register(Contract)
