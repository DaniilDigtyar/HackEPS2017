from django.db import models

class Users(models.Model):
    user = models.TextField()

    def __str__(self):
        return self.name

# Create your models here.
