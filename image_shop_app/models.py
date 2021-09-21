from django.db import models
class User(models.Model):
    cart_item = models.BooleanField(default = False)
    
    
class Images(models.Model):
    image_data = models.ForeignKey(User, on_delete=models.CASCADE)
    image_id = models.CharField(max_length = 30)
    image_alt_description = models.TextField()
    image_url = models.URLField()





    



# Create your models here.
