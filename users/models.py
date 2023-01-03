from django.db import models
from django.contrib.auth.models import User


# Create your models here.

def user_directory_path(instance, filename):
        # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
        filename = '%s.jpg'%instance.user.username
        return '{0}/{1}'.format('profile_pictures', filename)
    
class Profile(models.Model):
    
    
    def __str__(self):
        
        return self.user.username
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='profile.jpg',upload_to=user_directory_path)
    contact_number = models.CharField(max_length=100,default="9999999999")
    
    