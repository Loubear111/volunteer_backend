from django.db import models

# Create your models here.

class user(models.Model):
	username = models.CharField(max_length=100,primary_key=True)
	name = models.CharField(max_length=100)
	points = models.IntegerField()
	location = models.CharField(max_length=300)

class organization(models.Model):
	name = models.CharField(max_length=300)
	username = models.CharField(max_length=100,primary_key=True)
	location = models.CharField(max_length=300)

class event(models.Model):
	longitude = models.FloatField()
	latitude = models.FloatField(default=0.0,null=True,blank=True)
	num_people = models.IntegerField()
	start_time = models.CharField(max_length=100)
	end_time = models.CharField(max_length=100)
	pph = models.IntegerField()
	eid = models.IntegerField(primary_key=True)
	name = models.CharField(max_length=300)
	host_org = models.ForeignKey(organization,on_delete=models.PROTECT)

class event_user_junction(models.Model):
	username = models.ForeignKey(user,on_delete=models.PROTECT)
	eid = models.ForeignKey(event,on_delete=models.PROTECT)
