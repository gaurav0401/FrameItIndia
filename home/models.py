from django.db import models
#user gaurav21 pass Bhatt21
# Create your models here.


class Images(models.Model):
    photo=models.ImageField()
    date=models.DateTimeField(auto_now_add=True)
