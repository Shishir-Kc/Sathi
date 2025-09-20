from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

class Sathi_User(AbstractUser):
    id = models.UUIDField(default=uuid.uuid4,primary_key=True,verbose_name="user_id",editable=False)
    User_image = models.ImageField(upload_to="Sathi/User/images/",blank=True)
