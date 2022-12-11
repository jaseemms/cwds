# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,get_object_or_404
from cwds.decorators import check_group,check_user
from django.contrib.auth.decorators import login_required
from myuser.models import MyUser
from models import MailBox,Product,Order,Contact,Donation,AgencyPlant,UserAgency
from forms import MailBoxForm,ProductForm,OrderForm,ContactForm,DonationForm,OrderStatusForm
from django.http.response import HttpResponseRedirect
from django.core.urlresolvers import reverse


def index(request):
	context = {
		'title':'Home'
	}
	return render(request,'general/index.html',context)


def about(request):
	context ={
		'title': 'About',
	}
	return render(request,'general/about.html',context)
	

@login_required(login_url='/login/')
@check_user('/login/','admin')
@check_group(['admin'])
def admin_dashboard(request):
	context = {
		'title':'Admin Dashboard'
	}
	return render(request,'general/admin_dashboard.html',context)


@login_required(login_url='/agency-login/')
@check_user('/agency-login/','agency')
@check_group(['agency'])
def agency_dashboard(request):
	context = {
		'title':'Agency Dashboard'
	}
	return render(request,'general/agency_dashboard.html',context)


@login_required(login_url='/plant-login/')
@check_user('/plant-login/','plant')
@check_group(['plant'])
def plant_dashboard(request):
	context = {
		'title':'Plant Dashboard'
	}
	return render(request,'general/plant_dashboard.html',context)


@login_required(login_url='/user-login/')
@check_user('/user-login/','user')
@check_group(['user'])
def user_dashboard(request):
	context = {
		'title':'User Dashboard'
	}
	return render(request,'general/user_dashboard.html',context)



@login_required(login_url='/login/')
@check_group(['admin'])
def agency_confirm(request):

	a = request.GET.get('a')
	if a:
		MyUser.objects.filter(pk=a).update(is_active=True)

	instances = MyUser.objects.filter(user_type='agency',is_active=False,email_confirmation=True)
	context ={
		'title':'Agency Confirm',
		'instances':instances
	}
	return render(request,'general/agency_confirm.html',context)


@login_required(login_url='/login/')
@check_group(['admin'])
def plant_confirm(request):

	p = request.GET.get('p')
	if p:
		MyUser.objects.filter(pk=p).update(is_active=True)

	instances = MyUser.objects.filter(user_type='plant',is_active=False,email_confirmation=True)
	context ={
		'title':'Plant Confirm',
		'instances':instances
	}
	return render(request,'general/plant_confirm.html',context)


@login_required(login_url='/login/')
@check_group(['admin'])
def user_confirm(request):

	u = request.GET.get('u')
	if u:
		MyUser.objects.filter(pk=u).update(is_active=True)

	instances = MyUser.objects.filter(user_type='user',is_active=False,email_confirmation=True)
	context ={
		'title':'User Confirm',
		'instances':instances
	}
	return render(request,'general/user_confirm.html',context)


@login_required(login_url='/')
@check_group(['admin','agency','user'])
def create_mail(request):
	if request.user.is_superuser:
		to = MyUser.objects.filter(user_type='agency')
	elif request.user.user_type == 'agency':
		to = MyUser.objects.exclude(user_type__in=['agency','plant'])
		not_agencyuser = set(UserAgency.objects.exclude(agency=request.user,state='complete').values('user'))
		to = to.exclude(pk__in=not_agencyuser)
	else:
		to = MyUser.objects.exclude(user_type__in=['agency','user','plant'])

	if request.method == 'POST':
		form = MailBoxForm(request.POST)
		if form.is_valid():
			data = form.save(commit=False)
			data.creator = request.user
			data.save()
			form = MailBoxForm()
			form.fields['to'].queryset = to
			context ={
				'form': form,
				'message': 'Message sent Successfully',
				'title': 'Create Mail',
			}
		else:
			form.fields['to'].queryset = to
			context = {
				'form':form,
				'title':'Create Mail',
			}
	else:
		form = MailBoxForm()
		form.fields['to'].queryset = to
		context = {
			'form':form,
			'title':'Create mail',
		}
	return render(request,'general/create_mail.html',context)


@login_required(login_url='/')
@check_group(['admin','agency','user'])
def sent_mail(request):
	instances = MailBox.objects.filter(creator=request.user.pk,sentitems_deleted=False)
	
	context = {
		'instances':instances,
		'title':'Send Mail'
	}
	return render(request,'general/send_mail.html',context)


@login_required(login_url='/')
@check_group(['admin','agency','user'])
def received_mail(request):
	instances = MailBox.objects.filter(to=request.user.pk,inbox_deleted=False)
	
	context = {
		'instances':instances,
		'title':'Received Mail'
	}
	return render(request,'general/received_mail.html',context)


@login_required(login_url='/')
@check_group(['admin','agency','user'])
def inbox_deleted(request,pk):
	instance = MailBox.objects.filter(pk=pk).update(inbox_deleted=True)
	return HttpResponseRedirect(reverse('general:received_mail'))


@login_required(login_url='/')
@check_group(['admin','agency','user'])
def sentitems_deleted(request,pk):
	instance = MailBox.objects.filter(pk=pk).update(sentitems_deleted=True)
	return HttpResponseRedirect(reverse('general:sent_mail'))

@login_required(login_url='/plant-login/')
@check_group(['plant'])
def create_product(request):
	if request.method == 'POST':
		form = ProductForm(request.POST,request.FILES)
		if form.is_valid():
			data = form.save(commit=False)
			data.plant = request.user
			data.save()
			return HttpResponseRedirect(reverse('general:view_product',kwargs={'pk':data.pk}))
		else:
			context = {
				'form':form,
				'title':'Create Product'
			}
	else:
		form = ProductForm()
		context = {
			'form':form,
			'title':'Create Product'
		}
	return render(request,'general/entry_product.html',context)


@login_required(login_url='/')
@check_group(['plant','admin'])
def edit_product(request,pk):
	instance = get_object_or_404(Product,pk=pk)
	if request.method == 'POST':
		form = ProductForm(request.POST,request.FILES,instance=instance)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('general:view_product',kwargs={'pk':form.instance.pk}))
		else:
			context = {
				'form':form,
				'title':'Edit Product'
			}
	else:
		form = ProductForm(instance=instance)
		context = {
			'form':form,
			'title':'Edit Product'
		}
	return render(request,'general/entry_product.html',context)


@login_required(login_url='/')
@check_group(['admin','user','plant'])
def view_product(request,pk):
	instance = get_object_or_404(Product,pk=pk)
	context = {
		'instance':instance,
		'title':'View Product'
	}
	return render(request,'general/view_product.html',context)


@login_required(login_url='/')
@check_group(['admin','user','plant'])
def view_products(request):
	if request.user.user_type == 'plant':
		instances = Product.objects.filter(is_deleted=False,plant=request.user)
	else:
		instances = Product.objects.filter(is_deleted=False)
	context ={
		'instances':instances,
		'title': 'View Products'
	}
	return render(request,'general/view_products.html',context)


@login_required(login_url='/')
@check_group(['plant','admin'])
def delete_product(request,pk):
	Product.objects.filter(pk=pk).update(is_deleted=True)
	return HttpResponseRedirect(reverse('general:view_products'))


@login_required(login_url='/user-login/')
@check_group(['user'])
def create_order(request,product_id):
	product = get_object_or_404(Product,pk=product_id)

	if request.method == 'POST':
		form = OrderForm(request.POST)
		if form.is_valid():

			order_id = 1
			order_obj = Order.objects.filter(product__plant=product.plant)
			if order_obj.exists():
				order_id = order_obj.latest('id').order_id + 1

			data = form.save(commit=False)
			data.user = request.user
			data.product = product
			data.order_id = order_id
			data.state = 'processing'
			data.total_price = data.quantity * data.product.price
			data.save()
			return HttpResponseRedirect(reverse('general:view_orders'))
		else:
			context = {
				'form':form,
				'product':product,
				'title':'Create Order'
			}
	else:
		form = OrderForm()
		context = {
			'form':form,
			'product':product,
			'title':'Create Order'
		}
	return render(request,'general/create_order.html',context)


@login_required(login_url='/')
@check_group(['plant','admin'])
def view_order(request,pk):
	instance = get_object_or_404(Order,pk=pk)
	context = {
		'instance':instance,
		'title':'View Order'
	}
	return render(request,'general/view_order.html',context)


@login_required(login_url='/plant-login/')
@check_group(['plant'])
def change_order_status(request,pk):
	instance = get_object_or_404(Order,pk=pk)
	if request.method == 'POST':
		form = OrderStatusForm(request.POST,instance=instance)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('general:view_orders'))
		else:
			form.fields['state'].choices = (('processing','Processing'),('payment','Payment'),('shipped','Shipped'))
			form.fields['state'].initial = instance.state
			context ={
				'form':form,
				'instance':instance,
				'title':'Change Status'
			}
	else:
		form = OrderStatusForm()
		form.fields['state'].choices = (('processing','Processing'),('payment','Payment'),('shipped','Shipped'))
		form.fields['state'].initial = instance.state
		context = {
			'form':form,
			'instance':instance,
			'title':'Change Status'
		}
	return render(request,'general/change_order_status.html',context)


@login_required(login_url='/')
@check_group(['user','admin','plant'])
def view_orders(request):
	if request.user.user_type == 'user':
		instances = Order.objects.filter(user=request.user).exclude(state='cancel')
	elif request.user.is_superuser:
		instances = Order.objects.exclude(state='cancel')
	else:
		instances = Order.objects.filter(product__plant=request.user,state__in=['processing','payment','shipped'])
	context = {
		'instances':instances,
		'title':'View Orders'
	}
	return render(request,'general/view_orders.html',context)


@login_required(login_url='/user-login/')
@check_group(['user'])
def delete_order(request,pk):
	Order.objects.filter(pk=pk).update(state='cancel')
	return HttpResponseRedirect(reverse('general:view_orders'))



def create_contact(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			name = form.cleaned_data['name']
			email = form.cleaned_data['email']
			subject = form.cleaned_data['subject']
			message = form.cleaned_data['message']
			form.save()

			admins = MyUser.objects.filter(is_active=True,is_staff=True)
			message = "New Contact Submitted\
			name: %s, email: %s, subject: %s, message : %s" %(name,email,subject,message)
			for admin in admins:
				MailBox(
					to = admin,
					message = message
				).save()

			context = {
				'message':'New contact Submitted',
				'form':ContactForm(),
				'title':'Create Contact'
			}
		else:
			context = {
				'form' : form,
				'title' : 'Create Contact'
			}
	else:
		form = ContactForm()
		context = {
			'form':form,
			'title':'Create Contact'
		}
	return render(request,'general/create_contact.html',context)


def create_donation(request):
	if request.method == 'POST':
		form = DonationForm(request.POST)
		if form.is_valid():
			name = form.cleaned_data['name']
			email = form.cleaned_data['email']
			donation_type = form.cleaned_data['donation_type']
			donation_amount = form.cleaned_data['donation_amount']
			form.save()

			admins = MyUser.objects.filter(is_active=True,is_staff=True)
			message = '''New Donation Submitted
			name: %s, email: %s, donation type: %s, donation amount : %s''' %(name,email,dict(form.fields['donation_type'].choices)[donation_type],dict(form.fields['donation_amount'].choices)[donation_amount])
			for admin in admins:
				MailBox(
					to = admin,
					message = message
					).save()

			context = {
				'message': 'Submitted Succesfully',
				'form':DonationForm(),
				'title':'Create Donation'
			}
		else:
			context = {
				'form' : form,
				'title' : 'Create Donation'
			}
	else:
		form = DonationForm()
		context = {
			'form':form,
			'title':'Create Donation'
		}
	return render(request,'general/create_donation.html',context)


@login_required(login_url='/plant-login/')
@check_group(['plant'])
def view_plant_requests(request):
	instances = AgencyPlant.objects.filter(status='request')
	context = {
		'title': 'View Request',
		'instances':instances
	}
	return render(request,'general/view_plant_requests.html',context)


@login_required(login_url='/plant-login/')
@check_group(['plant'])
def complete_plant_request(request,pk):
	AgencyPlant.objects.filter(pk=pk).update(status='complete')
	return HttpResponseRedirect(reverse('general:view_plant_requests'))


@login_required(login_url='/agency-login/')
@check_group(['agency'])
def select_plant(request,plant_id):
	agencyplant = AgencyPlant.objects.filter(plant=plant_id,agency_user=request.user.pk)

	if agencyplant.exists():
		request.session['message'] = 'You Already Selected This Plant'
	else:
		plant = get_object_or_404(MyUser,pk=plant_id)
		AgencyPlant(
			plant= plant,
			agency_user = request.user,
			status = 'select'
			).save()
	return HttpResponseRedirect(reverse('general:request_plant'))


@login_required(login_url='/agency-login/')
@check_group(['agency'])
def request_plant(request):
	instances = AgencyPlant.objects.filter(agency_user=request.user.pk,status__in=['select','request'])

	try:
		message = request.session['message']
		del request.session['message']
	except:
		message = None

	context = {
		'instances': instances,
		'title': 'Request Plant',
		'message': message
	}
	return render(request,'general/request_plant.html',context)


@login_required(login_url='/agency-login/')
@check_group(['agency'])
def request_plant_confirm(request,plant_id):
	AgencyPlant.objects.filter(plant=plant_id,agency_user=request.user.pk).update(status='request')
	return HttpResponseRedirect(reverse('general:request_plant'))


@login_required(login_url='/agency-login/')
@check_group(['agency'])
def removeplant(request,pk):
	AgencyPlant.objects.filter(pk=pk).delete()
	return HttpResponseRedirect(reverse('myuser:view_agency',kwargs={'pk':request.user.pk}))


@login_required(login_url='/agency-login/')
@check_group(['agency'])
def view_agency_request(request):
	instances = UserAgency.objects.filter(state='request',agency=request.user)
	context = {
		'instances':instances,
		'title': 'View Request'
	}
	return render(request,'general/view_agency_request.html',context)


@login_required(login_url='/agency-login/')
@check_group(['agency'])
def conform_agency_user(request,pk):
	agencyuser = UserAgency.objects.filter(pk=pk).update(state='complete')
	return HttpResponseRedirect(reverse('general:view_agency_request'))


def removeagency(request,pk):
	UserAgency.objects.filter(pk=pk).delete()
	return HttpResponseRedirect(reverse('myuser:view_user',kwargs={'pk': request.user.pk }))


@login_required(login_url='/')
@check_group(['agency','user','admin'])
def mailbox(request):
	if request.user.is_superuser:
		title = 'Feedback'
		base_template = 'general/admin_dashboard.html'
	elif request.user.user_type == 'user':
		title = 'Feedback'
		base_template = 'general/user_dashboard.html'
	else:
		title = 'Warnings'
		base_template = 'general/agency_dashboard.html'

	inboxes = MailBox.objects.filter(to=request.user,inbox_deleted=False).count()
	sent_items = MailBox.objects.filter(creator=request.user,sentitems_deleted=False).count()

	context ={
		'title':title,
		'inboxes':inboxes,
		'sent_items':sent_items,
		'base_template': base_template
	}
	return render(request,'general/mailbox.html',context)


@login_required(login_url='/user-login/')
@check_group(['user'])
def select_agency(request,agency_id):
	useragency = UserAgency.objects.filter(agency=agency_id,user=request.user.pk)
	current_limit = UserAgency.objects.filter(agency=agency_id,state='complete').count()

	agency_limit = get_object_or_404(MyUser,pk=agency_id).agency_limit

	if useragency.exists():
		request.session['message'] = 'You Already Selected This Agency'
	elif UserAgency.objects.filter(user=request.user.pk).exists():
		request.session['message'] = 'You Already Selected An Agency'
		return HttpResponseRedirect(reverse('myuser:view_agencies'))
	elif current_limit >= agency_limit:
		request.session['message'] = 'Agency Limit passed'
		return HttpResponseRedirect(reverse('myuser:view_agencies'))
	else:
		agency = get_object_or_404(MyUser,pk=agency_id)
		UserAgency(
			agency= agency,
			user = request.user,
			state = 'select'
			).save()
	return HttpResponseRedirect(reverse('general:request_agency'))


@login_required(login_url='/user-login/')
@check_group(['user'])
def request_agency(request):
	instances = UserAgency.objects.filter(user=request.user.pk,state__in=['select','request'])

	try:
		message = request.session['message']
		del request.session['message']
	except:
		message = None

	context = {
		'instances': instances,
		'title': 'Request Agency',
		'message': message
	}
	return render(request,'general/request_agency.html',context)


@login_required(login_url='/user-login/')
@check_group(['user'])
def request_agency_confirm(request,agency_id):
	current_limit = UserAgency.objects.filter(agency=agency_id,state='complete').count()
	agency_limit = get_object_or_404(MyUser,pk=agency_id).agency_limit
	if current_limit >= agency_limit:
		request.session['message'] = 'Agency limit passed.'
	else:
		UserAgency.objects.filter(agency=agency_id,user=request.user.pk).update(state='request')
	return HttpResponseRedirect(reverse('general:request_agency'))