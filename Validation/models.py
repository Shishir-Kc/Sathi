from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

class Sathi_User(AbstractUser):
    id = models.UUIDField(default=uuid.uuid4,primary_key=True,verbose_name="user_id",editable=False)




class Images(models.Model):
    user = models.ForeignKey(Sathi_User, verbose_name="User_Name", on_delete=models.CASCADE)
    id = models.UUIDField(default=uuid.uuid4,primary_key=True,editable=False)
    image_name = models.CharField(max_length=256)
    image_url = models.URLField(max_length=500)

    class Meta:
        verbose_name = 'Image'
        verbose_name_plural = 'Images'

    