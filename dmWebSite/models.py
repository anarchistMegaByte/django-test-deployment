from django.db import models

# Create your models here.
class dmWebsiteUser(models.Model):
    user_name = models.CharField(max_length=50)
    user_email = models.CharField(max_length=50)
    user_phone = models.CharField(max_length=10)