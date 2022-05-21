from django.db import models
from items.models import Item

class Contract(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=500,null=True, blank=True)
    item = models.ForeignKey('items.Item', on_delete=models.CASCADE)
    price = models.IntegerField(max_length=10, null=True, blank=True)
    start_date = models.DateField(auto_now_add=True)
    end_date = models.DateField(auto_now_add=True)
    # duration = models.IntegerField(end_date - start_date)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name

def get_duration():
    duration= Contract.date_end - Contract.date_start
    return duration