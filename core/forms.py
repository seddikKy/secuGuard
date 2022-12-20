from django import forms
from django.forms import ModelForm
from .models import *
from django.contrib import admin 



#Create a Entreprise form
class EntrepriseFrom(ModelForm):
    class Meta:
        model = Entreprise
        fields = ('name','address','email','phone','RC','NIF') #"__all__"
        labels = {
            'name':'Nom de l\'entreprise',
            'address': 'Adresse de l\'entreprise',
            'email':'E-mail de l\'entreprise',
            'phone':'N° de tel de l\'entreprise',
            'RC': 'N° registre de commerce',
            'NIF':'N° identifiant fiscal',
        }
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control'}),#form-control : it's from bootstrap 
            'address': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class':'form-control'}),
            'phone':forms.TextInput(attrs={'class':'form-control'}),
            'RC':forms.TextInput(attrs={'class':'form-control'}),
            'NIF':forms.TextInput(attrs={'class':'form-control'}),
        }

#Create a Site form
class SiteFrom(ModelForm):
    class Meta:
        model = Site
        fields = ('name','id_entreprise', 'address','email','phone','RC','NIF') #"__all__"
        labels = {
            'name':'Nom de site',
            'id_entreprise':'Entreprise',
            'address': 'Adresse de site',
            'email':'E-mail de site',
            'phone':'N° de tel de site',
            'RC': 'N° registre de commerce',
            'NIF':'N° identifiant fiscal',
        }
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control'}),#form-control : it's from bootstrap 
            'id_entreprise':forms.Select(attrs={'class':'form-select'}),
            'address': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class':'form-control'}),
            'phone':forms.TextInput(attrs={'class':'form-control'}),
            'RC':forms.TextInput(attrs={'class':'form-control'}),
            'NIF':forms.TextInput(attrs={'class':'form-control'}),
        }

#Create a Site form
class ZoneFrom(ModelForm):
    class Meta:
        model = Zone
        fields = ('name','id_site') #"__all__"
        labels = {
            'name':'Nom de zone',
            'id_site':'Site',
        }
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control'}),#form-control : it's from bootstrap 
            'id_site':forms.Select(attrs={'class':'form-select'}),
        }


#Create a Site form
class EmployeeFrom(ModelForm):
    class Meta:
        model = Employee
        fields = ('name','id_site', 'address','email','phone') #"__all__"
        labels = {
            'name':'Nom de l\'agent',
            'id_site':'Site',
            'address': 'Adresse de l\'agent',
            'email':'E-mail de l\'agent',
            'phone':'N° de tel de l\'agent',
        }
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control'}),#form-control : it's from bootstrap 
            'id_site':forms.Select(attrs={'class':'form-select'}),
            'address': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class':'form-control'}),
            'phone':forms.TextInput(attrs={'class':'form-control'}),
        }



class TagHeaderForm(forms.ModelForm):
    class Meta:
        model = TagHeader
        fields = ('id_zone', 'code_nfc','name','observation') # "__all__"

    labels = {
        'id_zone':'Zone',
        'code_nfc': 'Code NFC',
        'name':'Nom de TAG',
        #'order':'Ordre',
        'observation':'Observation',
    }
    widgets = {
        'id_zone':forms.Select(attrs={'class':'form-select'}),
        'code_nfc': forms.TextInput(attrs={'class':'form-control'}),
        'name':forms.TextInput(attrs={'class':'form-control'}),#form-control : it's from bootstrap 
        'observation':forms.TextInput(attrs={'class':'form-control'}),
    }
  