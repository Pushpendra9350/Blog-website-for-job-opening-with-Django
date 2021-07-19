from django.db import models
from django.contrib.auth.models import User
from PIL import Image
# Create your models here.

class profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    image = models.ImageField(default = 'default.jpg', upload_to = 'profile_pics')

    def __str__(self):
        return f'{self.user.username} profile'
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)
        rgb_im = img.convert('RGB')
        if rgb_im.height>300 or rgb_im.width>300:
            output=(300,300)
            rgb_im.thumbnail(output)
            rgb_im.save(self.image.path)