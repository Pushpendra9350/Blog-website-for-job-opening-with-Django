from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Profile model to store image for all users 
class profile(models.Model):

    # Here we are mapping(one-to-one) this model with User model to store a image with each user
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    # Image bydefault if any one is not providing any image.
    image = models.ImageField(default = 'default.jpg', upload_to = 'profile_pics')

    # String when we query image for a loggedin user
    def __str__(self):
        return f'{self.user.username} profile'
    
    # Now reshape and save that image to database
    def save(self, *args, **kwargs):
        # This is a type of rule to write this
        super().save(*args, **kwargs)
        # Using python image library 
        img = Image.open(self.image.path)
        rgb_im = img.convert('RGB')
        if rgb_im.height>300 or rgb_im.width>300:
            output=(300,300)
            rgb_im.thumbnail(output)
            rgb_im.save(self.image.path)