from django.db import models

# Create your models here.

class listing(models.Model):
    user_id = models.CharField(max_length=100)
    Name = models.CharField(max_length=100)
    email = models.EmailField()
    age = models.PositiveIntegerField()
class Booking(models.Model):
    user_id = models.CharField(max_length=100)
    Name = models.CharField(max_length=100)
    email = models.EmailField()
    age = models.PositiveIntegerField()
    def __str__(self):
        return self.name
