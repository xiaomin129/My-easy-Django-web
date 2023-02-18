from django.db import models

# Create your models here.
class WorkerInfo(models.Model):
    name = models.CharField(max_length=32,blank=False)
    password = models.CharField(max_length=64,blank=False)
    age = models.IntegerField(null=True, blank=True)
    sex = models.BooleanField(default=1,blank=False)

class ManageInfo(models.Model):
    name = models.CharField(max_length=32,blank=False)
    password = models.CharField(max_length=64,blank=False)
    system_name = models.CharField(max_length=32,blank=False)
    age = models.IntegerField(null=True, blank=True)

class Drugs(models.Model):
    name = models.CharField(max_length=32,blank=False)
    classification = models.BooleanField(null=True,blank=True)
    price = models.FloatField(blank=False)
    num = models.IntegerField(null=True,blank=True)
    unit = models.CharField(default='盒',max_length=8,blank=False)

class Log(models.Model):
    time = models.DateTimeField()
    worker_name = models.CharField(max_length=32,blank=False)
    drugs_name = models.CharField(max_length=32,blank=False)
    InOrOut = models.BooleanField(blank=False)
    num = models.IntegerField(blank=False)

class God(models.Model):
    name = models.CharField(max_length=32,blank=False)
    time = models.DateTimeField()
    phone = models.CharField(max_length=32,blank=False)
    drugs = models.CharField(default='999感冒灵',max_length=32,blank=False)
