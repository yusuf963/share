from django.db import models
from datetime import datetime
from django.conf import settings

class Contract(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=500,null=True, blank=True)
    carbon_emissions_reduced = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='owner')
    borrower = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='borrowers')
    price = models.IntegerField(null=True, blank=True)
    start_date = models.DateField(default=datetime.now, blank=True)
    end_date = models.DateField(default=datetime.now, blank=True)
    duration = models.IntegerField(default=0, null=True, blank=True)
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    updated_at = models.DateTimeField(default=datetime.now, blank=True)
    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.duration = (self.end_date - self.start_date).total_seconds() / 3600 # lending duration per hours
        super().save(*args, **kwargs)
