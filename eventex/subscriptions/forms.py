# coding: utf-8
from django import forms


class SubscriptionForm(forms.Form):
    nome = forms.CharField()
    cpf = forms.CharField()
    email = forms.CharField()
    telefone = forms.CharField()