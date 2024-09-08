from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Diary_Model(models.Model):

    title=models.CharField(max_length=50)
    note=models.TextField()
    created_date=models.DateField(auto_now_add=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
