# coding: utf-8
from django.http import HttpResponseRedirect
from django.shortcuts import render
from eventex.subscriptions.forms import SubscriptionForm
from eventex.subscriptions.models import Subscription


def subscribe(request):
    if request.method == 'POST':
        return create(request)
    else:
        return new(request)

def new(request):
    return render(request, 'subscriptions/subscription_form.html', {'form': SubscriptionForm()})

def create(request):
    form = SubscriptionForm(request.POST)
    if form.is_valid():
        obj = form.save()
        return HttpResponseRedirect('/inscricao/%d/' % obj.pk)
    else:
        return render(request, 'subscriptions/subscription_form.html', {'form': form})