from django.test import TestCase
from eventex.subscriptions.forms import SubscriptionForm


class SubscriptFormTest(TestCase):
    def setUp(self):
        self.response = self.client.get('/inscricao/')

    def testFormHasFields(self):
        'Form must have 4 fields.'
        form = self.response.context['form']
        self.assertItemsEqual(['name', 'email', 'cpf', 'phone'], form.fields)
