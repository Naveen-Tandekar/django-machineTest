from django.db import models
from django.contrib.auth.models import User

class register(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    Mobile=models.IntegerField()
    age=models.IntegerField()
    Address=models.CharField(max_length=100)
    class Meta:
        db_table="register"

