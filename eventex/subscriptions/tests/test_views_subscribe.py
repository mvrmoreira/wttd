from django.test import TestCase
from eventex.subscriptions.forms import SubscriptionForm
from eventex.subscriptions.models import Subscription
from django.core.urlresolvers import reverse as r


class SubscriptTest(TestCase):
    def setUp(self):
        self.response = self.client.get(r('subscriptions:subscribe'))

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
        self.assertContains(self.response, 'type="text"', 4)
        self.assertContains(self.response, 'type="email"')
        self.assertContains(self.response, 'type="submit"')

    def testCsrf(self):
        'Html must contain csrf token.'
        self.assertContains(self.response, 'csrfmiddlewaretoken')

    def testHasForm(self):
        'Context must have the subscription form.'
        form = self.response.context['form']
        self.assertIsInstance(form, SubscriptionForm)


class SubscribePostTest(TestCase):
    def setUp(self):
        data = dict(
            name='Matheus Moreira',
            cpf='01234567890',
            email='matheus@moreira.com.br',
            phone='(21) 98888-7777'
        )
        self.response = self.client.post(r('subscriptions:subscribe'), data)

    def testPost(self):
        'Valid POST should redirect to /inscricao/1/'
        self.assertEqual(302, self.response.status_code)

    def testSave(self):
        'Valid POST must be saved.'
        self.assertTrue(Subscription.objects.exists())


class SubscribeInvalidPostTest(TestCase):
    def setUp(self):
        data = dict(
            name='Matheus Moreira',
            cpf='00000000000000000000',
            email='matheus@moreira.com.br',
            phone='(21) 98888-7777'
        )
        self.response = self.client.post(r('subscriptions:subscribe'), data)

    def testPost(self):
        'Invalid POST should not redirect.'
        self.assertEqual(200, self.response.status_code)

    def testFormErrors(self):
        'Form must contain errors.'
        self.assertTrue(self.response.context['form'].errors)

    def testDontSave(self):
        'Do not save data.'
        self.assertFalse(Subscription.objects.exists())


class TemplateRegressionTest(TestCase):
    def test_template_has_no_field_errors(self):
        'Check if non_field_errors are shown in template.'
        invalid_data = dict(name='Matheus Moreira', cpf='01234567890')
        response = self.client.post(r('subscriptions:subscribe'), invalid_data)

        self.assertContains(response, '<ul class="errorlist">')
