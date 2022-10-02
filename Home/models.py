import datetime

from django.contrib.auth.models import User
from django.db import models
from PIL import  Image
import os
from  django.utils import timezone
# Create your models here.

class Raw(models.Model):

    user=models.ForeignKey(User,on_delete=models.CASCADE)
    date=models.DateTimeField(null=True)

    im=models.ImageField(upload_to='RawImages')
    quality=models.IntegerField(default=30)
    def __str__(self):
        return  self.user
    def save(self):
        super().save()
        img = Image.open(self.im.path)
        self.size=os.path.getsize(self.im.path)
        print(self.size)
        # self.im=self.im.path+ran
        img.save(self.im.path, optimize=True, quality=self.quality)

class NoBG(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(null=True)

    img = models.ImageField(upload_to='NoBGImages')
    def __str__(self):
        return  self.user


