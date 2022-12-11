# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,get_object_or_404
from forms import MyUserCreationForm,MyUserChangeForm,PlantUserCreationForm,PlantUserChangeForm,\
LocationForm,AgencyLimitForm,AdminChangeForm
from models import MyUser,Location
from django.core.mail import send_mail
from django.http.response import HttpResponseRedirect
from django.core.urlresolvers import reverse
from cwds.decorators import check_group
from django.contrib.auth.decorators import login_required
from general.models import AgencyPlant,UserAgency


@login_required(login_url='/login/')
@check_group(['admin'])
def view_admin(request,pk):
	instance = get_object_or_404(MyUser,pk=pk)

	context = {
		'instance':instance,
		'title':'View Admin'
	}
	return render(request,'myuser/view_admin.html',context)


@login_required(login_url='/login/')
@check_group(['admin'])
def edit_admin(request,pk):
	instance = get_object_or_404(MyUser,pk=pk)
	if request.method == 'POST':
		form = AdminChangeForm(request.POST,instance=instance)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('myuser:view_admin',kwargs={'pk':form.instance.pk}))
		else:
			print 'error'
			context ={
				'form':form,
				'title': 'Edit Admin'
			}
	else:
		form = AdminChangeForm(instance=instance)
		context ={
			'form':form,
			'title':'Edit Admin'
		}
	return render(request,'myuser/edit_admin.html',context)


def create_agency(request):

	if request.method == 'POST':
		form = MyUserCreationForm(request.POST)
		if form.is_valid():
			data = form.save(commit=False)
			data.is_active = False
			data.user_type = 'agency'
			data.save()

			try:
				send_mail(
				    'New Registration',
				    'Click here for activating new account %s://%s/%s/%s' %(request.scheme,request.META.get('HTTP_HOST'),'verification',data.pk),
				    'from@example.com',
				    [data.email],
				    fail_silently=False,
				)
			except:
				data.delete()

				context = {
					'email': data.email,
					'title': 'Registration Failed'
				}
				return render(request,'myuser/registration_faild.html',context)

			context = {
				'email': data.email,
				'title': 'Registration Done'
			}
			return render(request,'myuser/registration_done.html',context)
		else:
			context = {
				'form': form,
				'title': 'Create Agency'
			}
	else:
		form = MyUserCreationForm()
		context = {
			'form':form,
			'title':'Create Agency'
		}
	return render(request,'myuser/create_agency.html',context)


@login_required(login_url='/agency-login/')
@check_group(['agency'])
def edit_agency(request,pk):
	instance = get_object_or_404(MyUser,pk=pk)

	if request.method == 'POST':
		form = MyUserChangeForm(request.POST,instance=instance)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('myuser:view_agency', kwargs={'pk': instance.pk}))
		else:
			context ={
				'form':form,
				'title':'Edit Agency'
			}
	else:
		form = MyUserChangeForm(instance=instance)
		context = {
			'form':form,
			'title': 'Edit Agency'
		}
	return render(request,'myuser/edit_agency.html',context)


@login_required(login_url='/agency-login/')
@check_group(['agency','admin'])
def view_agency(request,pk):
	instance = get_object_or_404(MyUser,pk=pk)
	plants = AgencyPlant.objects.filter(agency_user=request.user.pk,status='complete')

	context = {
		'instance':instance,
		'plants':plants,
		'title':'View Agency'
	}
	return render(request,'myuser/view_agency.html',context)


@login_required(login_url='/')
@check_group(['user','admin'])
def view_agencies(request):
	instances = MyUser.objects.filter(user_type='agency',is_active=True)
	if request.user.user_type == 'user':
		title = 'Select Agency'
	elif request.user.is_superuser:
		title = 'Registered Agency'

	try:
		message = request.session['message']
		del request.session['message']
	except:
		message = None

	context = {
		'instances': instances,
		'message': message,
		'title':title
	}
	return render(request,'myuser/view_agencies.html',context)


def create_user(request):

	if request.method == 'POST':
		form = MyUserCreationForm(request.POST)
		if form.is_valid():
			data = form.save(commit=False)
			data.is_active = False
			data.user_type = 'user'
			data.save()

			try:
				send_mail(
				    'New Registration',
				    'Click here for activating new account %s://%s/%s/%s' %(request.scheme,request.META.get('HTTP_HOST'),'verification',data.pk),
				    'from@example.com',
				    [data.email],
				    fail_silently=False,
				)
			except:
				data.delete()

				context = {
					'email': data.email,
					'title': 'Registration Faild'
				}
				return render(request,'myuser/registration_faild.html',context)

			context = {
				'email': data.email,
				'title': 'Registration Done'
			}
			return render(request,'myuser/registration_done.html',context)
		else:
			context = {
				'form': form,
				'title': 'Create User'
			}
	else:
		form = MyUserCreationForm()
		context = {
			'form':form,
			'title':'Create User'
		}
	return render(request,'myuser/create_user.html',context)


@login_required(login_url='/user-login/')
@check_group(['user'])
def edit_user(request,pk):
	instance = get_object_or_404(MyUser,pk=pk)

	if request.method == 'POST':
		form = MyUserChangeForm(request.POST,instance=instance)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('myuser:view_user', kwargs={'pk': instance.pk}))
		else:
			context ={
				'form':form,
				'title':'Edit User'
			}
	else:
		form = MyUserChangeForm(instance=instance)
		context = {
			'form':form,
			'title': 'Edit User'
		}
	return render(request,'myuser/edit_user.html',context)


@login_required(login_url='/user-login/')
@check_group(['user','admin'])
def view_user(request,pk):
	instance = get_object_or_404(MyUser,pk=pk)
	try:
		agency = get_object_or_404(UserAgency,user=request.user)
	except:
		agency = None

	context = {
		'instance':instance,
		'agency':agency,
		'title' :'View User'
	}
	return render(request,'myuser/view_user.html',context)


@login_required(login_url='/login/')
@check_group(['admin'])
def view_users(request):
	instances = MyUser.objects.filter(user_type='user',is_active=True)
	context ={
		'title' : 'View Users',
		'instances': instances
	}
	return render(request,'myuser/view_users.html',context)


def create_plant(request):

	if request.method == 'POST':
		form = PlantUserCreationForm(request.POST)
		if form.is_valid():
			data = form.save(commit=False)
			data.is_active = False
			data.user_type = 'plant'
			data.save()

			try:
				send_mail(
				    'New Registration',
				    'Click here for activating new account %s://%s/%s/%s' %(request.scheme,request.META.get('HTTP_HOST'),'verification',data.pk),
				    'from@example.com',
				    [data.email],
				    fail_silently=False,
				)
			except:
				data.delete()

				context = {
					'email': data.email,
					'title': 'Registration Faild'
				}
				return render(request,'myuser/registration_faild.html',context)

			context = {
				'email': data.email,
				'title': 'Registration Done'
			}
			return render(request,'myuser/registration_done.html',context)
		else:
			context = {
				'form': form,
				'title': 'Create Plant'
			}
	else:
		form = PlantUserCreationForm()
		context = {
			'form':form,
			'title':'Create Plant'
		}
	return render(request,'myuser/create_plant.html',context)


@login_required(login_url='/plant-login/')
@check_group(['plant'])
def edit_plant(request,pk):
	instance = get_object_or_404(MyUser,pk=pk)

	if request.method == 'POST':
		form = PlantUserChangeForm(request.POST,instance=instance)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('myuser:view_plant', kwargs={'pk': instance.pk}))
		else:
			context ={
				'form':form,
				'title':'Edit Plant'
			}
	else:
		form = PlantUserChangeForm(instance=instance)
		context = {
			'form':form,
			'title': 'Edit Plant'
		}
	return render(request,'myuser/edit_plant.html',context)


@login_required(login_url='/plant-login/')
@check_group(['plant','admin'])
def view_plant(request,pk):
	instance = get_object_or_404(MyUser,pk=pk)

	context = {
		'instance':instance,
		'title' :'View Plant'
	}
	return render(request,'myuser/view_plant.html',context)


@login_required(login_url='/')
@check_group(['agency','admin'])
def view_plants(request):
	instances = MyUser.objects.filter(is_active=True,user_type='plant')
	context ={
		'instances': instances,
		'title': 'View Plants'
	}
	return render(request,'myuser/view_plants.html',context)


def verification(request,pk):
	MyUser.objects.filter(pk=pk).update(email_confirmation=True)
	context ={
		'title':'Email Confirmation'
	}
	return render(request,'myuser/email_verification.html',context)


@login_required(login_url='/login/')
@check_group(['admin'])
def create_location(request):
	if request.method =='POST':
		form = LocationForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('myuser:create_location'))
		else:
			context = {
				'form':form,
				'title':'Create Location'
			}
	else:
		form = LocationForm()
		context ={
			'form':form,
			'title':'Create Location'
		}
	return render(request,'myuser/entry_location.html',context)


@login_required(login_url='/login/')
@check_group(['admin'])
def edit_location(request,pk):
	instance = get_object_or_404(Location,pk=pk)
	if request.method =='POST':
		form = LocationForm(request.POST,instance=instance)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('myuser:view_locations'))
		else:
			context = {
				'form':form,
				'title':'Edit Location'
			}
	else:
		form = LocationForm(instance=instance)
		context = {
			'form':form,
			'title':'Edit Location'
		}
	return render(request,'myuser/entry_location.html',context)


@login_required(login_url='/login/')
@check_group(['admin'])
def view_locations(request):
	instances = Location.objects.filter(is_deleted=False)
	context ={
		'instances':instances,
		'title':'View Locations'
	}
	return render(request,'myuser/view_locations.html',context)


@login_required(login_url='/login/')
@check_group(['admin'])
def delete_location(request,pk):
	Location.objects.filter(pk=pk).update(is_deleted=True)
	return HttpResponseRedirect(reverse('myuser:view_locations'))


@login_required(login_url='/login/')
@check_group(['admin'])
def agency_limit(request,pk):
	instance = get_object_or_404(MyUser,pk=pk)

	if request.method == 'POST':
		form = AgencyLimitForm(request.POST,instance=instance)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('myuser:agency_limits'))
		else:
			context = {
				'title':'Agency Limit',
				'form':form,
				'instance':instance
			}
	else:
		form = AgencyLimitForm(instance=instance)
		context = {
			'title':'Agency Limit',
			'form':form,
			'instance':instance
		}
	return render(request,'myuser/agency_limit.html',context)


@login_required(login_url='/login/')
@check_group(['admin'])
def agency_limits(request):
	instances = MyUser.objects.filter(user_type='agency',is_active=True)
	context = {
		'instances':instances,
		'title':'Agency Limits'
	}
	return render(request,'myuser/agency_limits.html',context)


