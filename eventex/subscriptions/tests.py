from django.test import TestCase
from eventex.subscriptions.forms import SubscriptionForm


class SubscriptTest(TestCase):
    def setUp(self):
        self.response = self.client.get('/inscricao/')

    def testGet(self):
        'GET /inscricao/ must return status code 200.'
        self.assertEqual(200, self.response.status_code)

    def testTemplate(self):
        'Response should be a rendered template.'
        self.assertTemplateUsed(self.response, 'subscriptions/subscription_form.html')

    def testHtml(self):
        'Html must contain input controls'
        self.assertContains(self.response, '<form')
        self.assertContains(self.response, '<input', 6)
        self.assertContains(self.response, 'type="text"', 3)
        self.assertContains(self.response, 'type="email"')
        self.assertContains(self.response, 'type="submit"')

    def testCsrf(self):
        'Html must contain csrf token.'
        self.assertContains(self.response, 'csrfmiddlewaretoken')

    def testHasForm(self):
        'Context must have the subscription form.'
        form = self.response.context['form']
        self.assertIsInstance(form, SubscriptionForm)

    def testFormHasFields(self):
        'Form must have 4 fields.'
        form = self.response.context['form']
        self.assertItemsEqual(['name', 'email', 'cpf', 'phone'], form.fields)
