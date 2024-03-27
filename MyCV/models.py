from django.db import models
from django.utils.html import mark_safe
# Create your models here.

class Berita(models.Model):

    title = models.CharField(max_length = 200)
    description = models.TextField(max_length = 900)
    pic = models.ImageField(upload_to='images', default='')
    def __str__(self):
        return f"{self.title} {self.description}"

    def image_tag(self):
        return mark_safe('<img src="%s" width="100px" height="100px" />'%(self.pic.url))
    image_tag.short_description = 'image'
    
class Review(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    review = models.TextField(max_length=500)
    datetime = models.DateTimeField(auto_now_add=True)
    img = models.ImageField(upload_to='images', default='')
    
    def image_tag(self):
        return mark_safe('<img src="%s" width="100px" height="100px" />'%(self.img.url))
    image_tag.short_description = 'image'