# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.core.validators import MinValueValidator

STATUS = (('select','Select'),('request','Request'),('complete','Complete'))
ORDER_CHOICE = (('processing','Processing'),('payment','Payment'),('shipped','Shipped'),('cancel','Cancel'))
DURATION = ((None, 'Select'),('one_time','One Time'),('monthly','Monthly'),('yearly','Yearly'))
DONATION_AMOUNT = ((None, 'Select'),(5,5),(10,10),(50,50))


class MailBox(models.Model):
	to = models.ForeignKey('myuser.MyUser',related_name='to')
	subject = models.CharField(max_length=128)
	message = models.TextField()
	is_read = models.BooleanField(default=False)
	creator = models.ForeignKey('myuser.MyUser',null=True,related_name='creator')
	date = models.DateTimeField(auto_now_add=True)
	inbox_deleted = models.BooleanField(default=False)
	sentitems_deleted = models.BooleanField(default=False)


class Product(models.Model):
	product_code = models.CharField(max_length=128)
	product_name = models.CharField(max_length=128)
	plant = models.ForeignKey('myuser.MyUser',limit_choices_to={'user_type':'plant'})
	description = models.TextField()
	price = models.FloatField()
	image = models.ImageField()
	is_deleted = models.BooleanField(default=False)


class Order(models.Model):
	order_id = models.PositiveIntegerField(validators=[MinValueValidator(1)])
	product = models.ForeignKey('general.Product')
	user = models.ForeignKey('myuser.MyUser',limit_choices_to={'user_type':'user'})
	quantity = models.PositiveIntegerField(validators=[MinValueValidator(1)])
	state = models.CharField(max_length=20,choices=ORDER_CHOICE)
	total_price = models.FloatField()
	date = models.DateField(auto_now_add=True)


class Contact(models.Model):
	name = models.CharField(max_length=128)
	email = models.EmailField()
	subject = models.CharField(max_length=128)
	message = models.TextField(max_length=256)


class Donation(models.Model):
	donation_amount = models.FloatField(choices=DONATION_AMOUNT)
	donation_type = models.CharField(max_length=20,choices=DURATION)
	name = models.CharField(max_length=128)
	email = models.EmailField()
	comment = models.TextField(max_length=256)


class UserAgency(models.Model):
	user = models.OneToOneField('myuser.MyUser',limit_choices_to={'user_type':'user'},related_name='user')
	agency = models.ForeignKey('myuser.MyUser',limit_choices_to={'user_type':'agency'},related_name='agency')
	state = models.CharField(max_length=20,choices=STATUS)


class AgencyPlant(models.Model):
	agency_user = models.ForeignKey('myuser.MyUser',limit_choices_to={"user_type":"agency"},
		related_name='agency_user')
	plant = models.ForeignKey('myuser.MyUser',limit_choices_to={"user_type":"plant"},
		related_name='agency_plant')
	status = models.CharField(max_length=20,choices=STATUS)


