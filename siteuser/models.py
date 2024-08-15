from django.db import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator
from cloudinary.models import CloudinaryField
from django.core.exceptions import ValidationError
from cloudinary import CloudinaryResource

#Create your models here.
def validate_cloudinary_file_extension(value):
    """
    Validate cloudinary files 
    """ 
    if isinstance(value, CloudinaryResource):
        extension = value.public_id.split('.')[-1].lower()
    else:
        extension = value.name.split('.')[-1].lower()

    valid_extensions = ['png', 'jpg']
    if extension not in valid_extensions:
        raise ValidationError(f'Unsupported file extension: {extension}. Allowed extensions are: {", ".join(valid_extensions)}')


class ProfileModel(models.Model):
    """
    Display user Profile
    """    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = CloudinaryField('image', default='default.png')
    def __str__(self):
        return self.user.username
