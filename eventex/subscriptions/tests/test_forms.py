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

    def test_cpf_is_digit(self):
        'CPF must only accept digits.'
        form = self.make_validated_form(cpf='ABCD5678901')
        self.assertItemsEqual(['cpf'], form.errors)

    def test_cpf_has_11_digits(self):
        'CPF must have 11 digits.'
        form = self.make_validated_form(cpf='1234')
        self.assertItemsEqual(['cpf'], form.errors)

    def make_validated_form(self, **kwargs):
        data = dict(name='Matheus Moreira', email='matheus@moreira.com', cpf='01234567890', phone='21-96186180')
        data.update(kwargs)
        form = SubscriptionForm(data)
        form.is_valid()
        return form

