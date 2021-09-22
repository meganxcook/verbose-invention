from django.db import models
from django.contrib.auth.models import User


class Image(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cart_item = models.BooleanField(default = True)
    owned_item = models.BooleanField(default = False)
    image_id = models.CharField(max_length = 30)
    image_alt_description = models.TextField()
    image_url = models.URLField()
    thumb_url = models.URLField()









# Create your models here.
