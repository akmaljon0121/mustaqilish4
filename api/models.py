from django.db import models

# Create your models here.
class Users(models.Model):
    id = id
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=16)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    come_to = models.DateTimeField(auto_now_add=True)

    def  __str__(self) -> str:
        return self.username

    
    
