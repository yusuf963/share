from django.db import models
import datetime
from django.conf import settings
from tinymce import models as tinymce_models
from _general_utility.token_generator import generate_model_code


# Generate token
def generate_blog_post_code():
    return f"ART_{generate_model_code(Article, 5)}"

class Article(models.Model):
     code = models.CharField(max_length=50, default=generate_blog_post_code, unique=True)
     test = models.CharField(max_length=100, unique=True, blank=True, null=True)
     title = models.CharField(max_length=355)
     author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL,null=True, related_name='articles')
     short_title = models.CharField(max_length=200, null=True, blank=False)
     is_published = models.BooleanField(default=False)
     publish_date = models.DateTimeField(blank=True, null=True)
     body = tinymce_models.HTMLField()
     hero_image = models.ImageField(upload_to='share/photos/articles/%Y/%m/%d/',null=True, blank=True)
     image1 = models.ImageField(upload_to='share/photos/articles/%Y/%m/%d/',null=True, blank=True)
     image2 = models.ImageField(upload_to='share/photos/articles/%Y/%m/%d/',null=True, blank=True)
     image3 = models.ImageField(upload_to='share/photos/articles/%Y/%m/%d/',null=True, blank=True)

     def save(self, *args, **kwargs):
        if self.is_published:
           self.publish_date = datetime.datetime.now()
        super().save(*args, **kwargs)
    
     def __str__(self):
        return self.title

     def summary(self):
        return self.body[:100]

     def pub_date_pretty(self):
        return self.publish_date.strftime('%b %e %Y')
