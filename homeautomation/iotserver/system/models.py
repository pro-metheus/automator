from django.db import models
from .choices import highlow
# Create your models here.
import uuid
from django.db import models
from django.contrib.auth.models import User

class Device(models.Model):
    user=models.ForeignKey(User)
    name=models.CharField(max_length=20)
    uid=models.UUIDField(default=uuid.uuid4().hex,unique=True)
    pin=models.CharField(max_length=2)
    state=models.CharField(max_length=1,choices=highlow)

    def __str__(self):
        return self.name




