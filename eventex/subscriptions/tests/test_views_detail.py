# coding: utf-8
from django.test import TestCase
from eventex.subscriptions.models import Subscription
from django.core.urlresolvers import reverse as r


class DetailTest(TestCase):
    def setUp(self):
        s = Subscription.objects.create(
            name='Matheus Moreira',
            cpf='01234567890',
            email='matheus@moreira.com.br',
            phone='(21) 98888-7777'
        )
        self.response = self.client.get(r('subscriptions:detail', args=[s.pk]))

    def testGet(self):
        'GET /inscricao/1/ should return status 200.'
        self.assertEqual(200, self.response.status_code)

    def testTemplate(self):
        'Uses template'
        self.assertTemplateUsed(self.response, 'subscriptions/subscription_detail.html')

    def testContext(self):
        'Context must have a subscription instance.'
        subscription = self.response.context['subscription']
        self.assertIsInstance(subscription, Subscription)

    def testHTML(self):
        'Check if subscription data was rendered.'
        self.assertContains(self.response, 'Matheus Moreira')


class DetailNotFound(TestCase):
    def testNotFound(self):
        response = self.client.get(r('subscriptions:detail', args=[0]))
        self.assertEqual(404, response.status_code)