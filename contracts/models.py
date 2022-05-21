from django.db import models
from items.models import Item
from django.contrib.auth.models import User
from datetime import datetime

class Contract(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=500,null=True, blank=True)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    owner = models.ForeignKey(User, related_name='owner', on_delete=models.CASCADE)
    borrower = models.ForeignKey(User, related_name='borrower', on_delete=models.CASCADE, null=True, blank=True)
    carbon_emissions_reduced = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)
    start_date = models.DateField(default=datetime.now, blank=True)
    end_date = models.DateField(default=datetime.now, blank=True)
    duration = models.IntegerField(default=0, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.duration = (self.end_date - self.start_date).total_seconds() / 3600 # lending duration per hours
        super().save(*args, **kwargs)