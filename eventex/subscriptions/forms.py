# coding: utf-8
from django import forms
from django.utils.translation import ugettext as _


class SubscriptionForm(forms.Form):
    name = forms.CharField(label=_('Nome'), widget=forms.TextInput(attrs={'class': 'form-control'}))
    cpf = forms.CharField(label=_('CPF'), widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label=_('Email'), widget=forms.EmailInput(attrs={'class': 'form-control'}))
    phone = forms.CharField(label=_('Telefone'), widget=forms.TextInput(attrs={'class': 'form-control'}))