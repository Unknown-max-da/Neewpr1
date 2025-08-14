from django.db import models

# Create your models here.

class Person(models.Model):
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)
    photo = models.ImageField(upload_to='media/photos/', blank=True,null=True)
    phone = models.CharField(max_length=120)

    def __str__(self):
        return self.first_name