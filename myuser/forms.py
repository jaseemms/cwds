from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from myuser.models import MyUser,Location
from django import forms
from django.forms.widgets import TextInput,Textarea,Select

class AdminChangeForm(forms.ModelForm):

    class Meta:
        model = MyUser
        fields =('username',)

        
class MyUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = MyUser
        fields = UserCreationForm.Meta.fields + ('address','location','pincode','contact_number','email','first_name')

    def __init__(self, *args, **kwargs):
        super(MyUserCreationForm, self).__init__(*args, **kwargs)
        self.fields.pop('password2')
        self.fields['location'].empty_label = 'Select Your Location'
   
    def save(self,commit=True):
        return super(MyUserCreationForm, self).save()
        if commit:
            user.save()
        return user

class MyUserChangeForm(forms.ModelForm):

    class Meta:
        model = MyUser
        fields = ('username','address','location','pincode','contact_number','email','first_name')

    def __init__(self, *args, **kwargs):
        super(MyUserChangeForm, self).__init__(*args, **kwargs)
        self.fields['location'].empty_label = 'Select Your Location'


class PlantUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = MyUser
        fields = UserCreationForm.Meta.fields + ('address','location','pincode','contact_number','email','first_name','plant_type')
        widgets = {
            'first_name': TextInput(attrs={'placeholder': 'Enter Plant Name','autofocus':''}),
            'address': TextInput(attrs={'placeholder': 'Enter Plant Address'}),
            'pincode': TextInput(attrs={'placeholder': 'Enter Plant Pincode'}),
            'email': TextInput(attrs={'placeholder': 'Enter Plant Email'}),
            'contact_number': TextInput(attrs={'placeholder': 'Enter Plant Contact Number'}),
            'username': TextInput(attrs={'placeholder': 'Enter a username'}),
        }

    def __init__(self, *args, **kwargs):
        super(PlantUserCreationForm, self).__init__(*args, **kwargs)
        self.fields.pop('password2')
        self.fields['location'].empty_label = 'Select Your Location'

   
    def save(self,commit=True):
        return super(PlantUserCreationForm, self).save()
        if commit:
            user.save()
        return user

class PlantUserChangeForm(forms.ModelForm):

    class Meta:
        model = MyUser
        fields = ('username','address','location','pincode','contact_number','email','first_name','plant_type')
        widgets = {
            'first_name': TextInput(attrs={'placeholder': 'Enter Plant Name','autofocus':''}),
            'address': TextInput(attrs={'placeholder': 'Enter Plant Address'}),
            'pincode': TextInput(attrs={'placeholder': 'Enter Plant Pincode'}),
            'email': TextInput(attrs={'placeholder': 'Enter Plant Email'}),
            'contact_number': TextInput(attrs={'placeholder': 'Enter Plant Contact Number'}),
            'username': TextInput(attrs={'placeholder': 'Enter a username'}),
        }

    def __init__(self, *args, **kwargs):
        super(PlantUserChangeForm, self).__init__(*args, **kwargs)
        self.fields['location'].empty_label = 'Select Your Location'


class LocationForm(forms.ModelForm):

    class Meta:
        model = Location
        fields = ('location',)
        widgets = {
            'location': TextInput(attrs={'placeholder': 'Enter Location'})
        }


class AgencyLimitForm(forms.ModelForm):

    class Meta:
        model = MyUser
        fields = ('agency_limit',)