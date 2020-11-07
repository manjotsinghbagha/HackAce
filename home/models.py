from django.db import models

# Create your models here.

class Image_for_ML(models.Model):
    image = models.ImageField(upload_to='ml_pics')

    def get_absolute_image_url(self):
        return "{0}{1}".format(settings.MEDIA_URL, self.image.url)