from django.db import models
from django.contrib.auth.models import User

class Item(models.Model):
    choice =(
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
    )
    name = models.CharField(max_length=100)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    description = models.TextField(max_length=500,null=True, blank=True)
    item_state = models.CharField(max_length=1, choices=choice, default='1')
    retail_price = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    hero_image = models.ImageField(upload_to='items/' )
    image1 = models.ImageField(upload_to='items/',null=True, blank=True)
    image2 = models.ImageField(upload_to='items/',null=True, blank=True)
    image3 = models.ImageField(upload_to='items/',null=True, blank=True)
    image4 = models.ImageField(upload_to='items/',null=True, blank=True)
    is_public = models.BooleanField(default=False)
    is_available = models.BooleanField(default=True)
    Address = models.ForeignKey(User, on_delete=models.CASCADE, related_name='items')
    door_number= models.CharField(max_length=10,null=True, blank=True)
    postcode = models.CharField(max_length=10, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    rate = models.IntegerField(default=0, null=True, blank=True)
    class Meta:
        verbose_name = 'Item'
        verbose_name_plural = 'Items'
    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    color_tag = models.CharField(max_length=7, default='#000000')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
    def __str__(self):
        return self.name