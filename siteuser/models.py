from django.db import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator
from cloudinary.models import CloudinaryField

# Create your models here.


class ProfileModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = CloudinaryField('image', default='default.png', validators=[FileExtensionValidator(['png', 'jpg'])])
    def __str__(self):
        return self.user.username
