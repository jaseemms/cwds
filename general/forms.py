from general.models import MailBox,Product,Order,Contact,Donation
from django import forms
from django.forms.widgets import TextInput,Textarea,Select


class MailBoxForm(forms.ModelForm):

	class Meta:
		model = MailBox
		fields = ('to','subject','message')


class ProductForm(forms.ModelForm):

	class Meta:
		model = Product
		fields = ('product_code','product_name','description','price','image')
		widgets ={
			'product_code': TextInput(attrs={'placeholder': 'Enter The Product Code'}),
			'product_name': TextInput(attrs={'placeholder': 'Enter The Product Name'}),
			'description' : Textarea(attrs={'placeholder': 'Enter The Product Description'}),
			'price': TextInput(attrs={'placeholder': 'Enter The Product Price'})
 		}


class OrderForm(forms.ModelForm):

	class Meta:
		model = Order
		fields =('quantity',)
		widgets ={
			'quantity': TextInput(attrs={'placeholder': 'Enter Quantity'}),
		}


class OrderStatusForm(forms.ModelForm):

	class Meta:
		model = Order
		fields = ('state',)

class ContactForm(forms.ModelForm):

	class Meta:
		model = Contact
		fields = ('name','email','subject','message')
		widgets = {
            'name': TextInput(attrs={'placeholder' : 'Name'}),
            'email': TextInput(attrs={'placeholder' : 'Email'}),
            'subject': TextInput(attrs={'placeholder' : 'Subject'}),
            'message': Textarea(attrs={'placeholder' : 'Message'}),
        }


class DonationForm(forms.ModelForm):

	class Meta:
		model = Donation
		fields = ('donation_amount','donation_type','name','email','comment')
		widgets = {
            'name': TextInput(attrs={'placeholder' : 'Name'}),
            'email': TextInput(attrs={'placeholder' : 'Email'}),
            'comment': Textarea(attrs={'placeholder' : 'Comment'}),
        }