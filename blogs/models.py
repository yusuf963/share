from django.db import models
from django.conf import settings
from general_utility.token_generator import generate_model_code
from tinymce import models as tinymce_models


#Generate token
def generate_blog_post_code():
    return f"BLO_{generate_model_code(BlogPost, 5)}"

class BlogPost(models.Model):
    code = models.CharField(max_length=100, unique=True ,default=generate_blog_post_code)
    title = models.CharField(max_length=355)
    short_title = models.CharField(max_length=200, null=True, blank=False)
    publish_date = models.DateTimeField()
    body = tinymce_models.HTMLField()
    hero_image = models.ImageField(upload_to='photos/blogs/%Y/%m/%d/',null=True, blank=True)
    image1 = models.ImageField(upload_to='photos/blogs/%Y/%m/%d/',null=True, blank=True)
    image2 = models.ImageField(upload_to='photos/blogs/%Y/%m/%d/',null=True, blank=True)
    image3 = models.ImageField(upload_to='photos/blogs/%Y/%m/%d/',null=True, blank=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING, related_name='blogs')
    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]

    def pub_date_pretty(self):
        return self.publish_date.strftime('%b %e %Y')


