from django.test import TestCase
from eventex.subscriptions.forms import SubscriptionForm
from django.core.urlresolvers import reverse as r


class SubscriptFormTest(TestCase):
    def setUp(self):
        self.response = self.client.get(r('subscriptions:subscribe'))

    def testFormHasFields(self):
        'Form must have 4 fields.'
        form = self.response.context['form']
        self.assertItemsEqual(['name', 'email', 'cpf', 'phone'], form.fields)
