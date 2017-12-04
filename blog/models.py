
# Create your models here.
from django.db import models


class userstest(models.Model):
    name = models.CharField(max_length=30)
    password = models.CharField(max_length=20)
