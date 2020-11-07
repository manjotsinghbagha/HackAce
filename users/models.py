from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    hight_in_cm = models.PositiveIntegerField(null=True)
    wight_in_kg = models.PositiveIntegerField(null=True)
    


    def __str__(self):
        return f'{self.user.username} Profile'


