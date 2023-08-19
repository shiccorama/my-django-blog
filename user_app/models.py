from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs) # we inherit from save-parent class and save the original image

        img = Image.open(self.image.path) # make new var for the original uploaded image.

        if img.height > 300 or img.width > 300:  # if height or width more than 300
            output_size = (300, 300)
            img.thumbnail(output_size) #, make it 300
            img.save(self.image.path) # save the resized image in the place of the original image.