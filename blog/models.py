
# Create your models here.
from django.db import models
import uuid
class rank(models.Model):
    rank_name=models.CharField(max_length=30)
    def __str__(self):
        return self.rank_name

class iden(models.Model):
    iden_name=models.CharField(max_length=30)
    def __str__(self):
        return self.iden_name

class userstest(models.Model):
    name = models.CharField(max_length=30)
    password = models.CharField(max_length=20)
    def __str__(self):
        return self.name

class admin(models.Model):
    uid=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=255)
    registerdate=models.DateField(max_length=255)

class item(models.Model):
    itemname=models.CharField(max_length=20)
    itemcost=models.CharField(max_length=20)
    itemtime=models.CharField(max_length=20)
    def __str__(self):
        return self.itemname

class coach(models.Model):
    uid=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=255)
    tel = models.CharField(max_length=11)
    gender=models.CharField(max_length=10)
    birth=models.DateField(max_length=10)
    charge=models.ForeignKey(item,null=False)
    registerdate=models.DateField(max_length=255)
    def __str__(self):
        return self.username

class userinfo(models.Model):
    username = models.CharField(max_length=30,unique=True)
    email=models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    gender=models.CharField(max_length=10,null=True)
    birth=models.DateField(max_length=10)
    weight=models.FloatField(null=True)
    height=models.FloatField(null=True)
    registerdate=models.DateField(max_length=10)
    choice=models.ForeignKey(item,null=False)
    uid=models.UUIDField(default=uuid.uuid4,editable=False)
    def __str__(self):
        return self.username


class user_now(models.Model):
    uid=models.CharField(max_length=255)
    username = models.CharField(max_length=30,unique=True)
    weight=models.FloatField(null=False)
    height=models.FloatField(null=False)
    choice=models.ForeignKey(item,null=False)

class weekly_info(models.Model):
    uid=models.CharField(max_length=255)
    username = models.CharField(max_length=30,unique=True)
    choice=models.ForeignKey(item,null=False)
    week0 = models.FloatField(null=True)
    week1 = models.FloatField(null=True)
    week1_suggest=models.TextField(max_length=255,null=True)
    week2 = models.FloatField(null=True)
    week2_suggest = models.TextField(max_length=255, null=True)
    week3 = models.FloatField(null=True)
    week3_suggest = models.TextField(max_length=255, null=True)
    week4 = models.FloatField(null=True)
    week4_suggest = models.TextField(max_length=255, null=True)
    week5 = models.FloatField(null=True)
    week5_suggest = models.TextField(max_length=255, null=True)
    week6 = models.FloatField(null=True)
    week6_suggest = models.TextField(max_length=255, null=True)
    week7 = models.FloatField(null=True)
    week7_suggest = models.TextField(max_length=255, null=True)
    week8 = models.FloatField(null=True)
    week8_suggest = models.TextField(max_length=255, null=True)
class testimgsrc(models.Model):
    name=models.CharField(max_length=255,null=True)
    path=models.CharField(max_length=255)