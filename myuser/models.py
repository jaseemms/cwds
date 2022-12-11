# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractUser

USER_TYPES = (('agency','Agency'),('plant','Plant'),('user','User'))
PLANT_TYPES = ((None,'Select'),('bio','Bio-degradable Plant'),('metal','Metal Plant'),('plastic','Plastic Plant'))
LIMIT = ((1,1),(100,100),(150,150),(200,200),(250,250),(300,300))


class MyUser(AbstractUser):
	email = models.EmailField(unique=True)
	address = models.CharField(max_length=128)
	location = models.ForeignKey('myuser.Location',null=True,limit_choices_to={"is_deleted":False})
	pincode = models.CharField(max_length=20)
	contact_number = models.CharField(max_length=20)
	user_type = models.CharField(max_length=12,choices=USER_TYPES)
	plant_type = models.CharField(max_length=10,choices=PLANT_TYPES,null=True)
	email_confirmation = models.BooleanField(default=False)
	agency_limit = models.PositiveIntegerField(choices=LIMIT,default=100)


class Location(models.Model):
	location = models.CharField(max_length=128)
	is_deleted = models.BooleanField(default=False)

	def __unicode__(self):
		return self.location
