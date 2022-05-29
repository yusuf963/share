from django.db import models
from django.conf import settings
# from typing import Type, TypeVar
# import os
# import binascii
from tinymce import models as tinymce_models
from general_utility.token_generator import generate_model_code


# Generate token
# def generate_token(size: int):
#     token = binascii.hexlify(os.urandom(size)).decode()
#     if len(token) > size:
#         return token[0:size].upper()
#     else:
#         return token.upper()

# M = TypeVar('M', bound=models.Model)

# def generate_model_code(cls: Type[M], min_size: int = 5, code_field: str = 'code'):
#     size = min_size
#     code = generate_token(size)
#     while cls.objects.filter(**{code_field: code}).exists():
#         size += 1
#         code = generate_token(size)
#     return code
def generate_blog_post_code():
    return f"Art_{generate_model_code(Article, 5)}"

class Article(models.Model):

     code = models.CharField(max_length=50,default=generate_blog_post_code ,   unique=True)
     test = models.CharField(max_length=100, unique=True, blank=True, null=True)
     title = models.CharField(max_length=355)
     short_title = models.CharField(max_length=200, null=True, blank=False)
     publish_date = models.DateTimeField()
     body = tinymce_models.HTMLField()
     hero_image = models.ImageField(upload_to='photos/blogs/%Y/%m/%d/',null=True, blank=True)
     image1 = models.ImageField(upload_to='photos/blogs/%Y/%m/%d/',null=True, blank=True)
     image2 = models.ImageField(upload_to='photos/blogs/%Y/%m/%d/',null=True, blank=True)
     image3 = models.ImageField(upload_to='photos/blogs/%Y/%m/%d/',null=True, blank=True)
     author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING, related_name='articles')
    
     def __str__(self):
        return self.title

     def summary(self):
        return self.body[:100]

     def pub_date_pretty(self):
        return self.publish_date.strftime('%b %e %Y')
