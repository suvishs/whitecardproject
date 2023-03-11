from django.forms import ModelForm
from django import forms
from whitecardapp . models import Application

class Applicationform(ModelForm):
    name = forms.CharField(max_length=20)
    last_name = forms.CharField(max_length=20)
    father_name = forms.CharField(max_length=20)
    phone_no = forms.IntegerField()
    Gender = forms.CharField(max_length=10)
    email = forms.EmailField()
    dob = forms.CharField(max_length=30)
    address = forms.CharField(max_length=250)
    aadhar_no = forms.IntegerField()
    license_no = forms.IntegerField()
    electionid_no = forms.CharField(max_length=15)
    rationcard_no = forms.IntegerField()
    Photo = forms.ImageField()

    class Meta:
        model = Application
        fields = ['name', 'last_name', 'father_name', 'phone_no', 'Gender', 
                  'email', 'dob', 'address', 'aadhar_no', 'license_no', 'electionid_no', 'rationcard_no', 'Photo']
        widget = {
            'name' : forms.TextInput(attrs={'class':'form-control'}),
            'last_name' : forms.TextInput(attrs={'class':'form-control'}),
            'father_name' : forms.TextInput(attrs={'class':'form-control'}),
            'phone_no' : forms.NumberInput(attrs={'class':'form-control'}),
            'gender' : forms.TextInput(attrs={'class':'form-control'}),
            'email' : forms.EmailInput(attrs={'class':'form-control'}),
            'dob' : forms.TextInput(attrs={'class':'form-control'}),
            'address' : forms.Textarea(attrs={'class':'form-control'}),
            'aadhar_no' : forms.NumberInput(attrs={'class':'form-control'}),
            'license_no' : forms.NumberInput(attrs={'class':'form-control'}),
            'electionid_no' : forms.TextInput(attrs={'class':'form-control'}),
            'rationcard_no' : forms.NumberInput(attrs={'class':'form-control'}),
            'Photo' : forms.FileInput(attrs={'class':'form-control'}),
        }