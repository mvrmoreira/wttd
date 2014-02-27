# coding: utf-8
from django.test import TestCase
from django.db import IntegrityError
from datetime import datetime
from eventex.subscriptions.models import Subscription


class SubscriptionTest(TestCase):
    def setUp(self):
        self.obj = Subscription(
            name='Matheus Moreira',
            cpf='01234567890',
            email='matheus@moreira.com.br',
            phone='(21) 98888-7777'
        )

    def testCreate(self):
        'Subscription must have name, cpf, email, phone'
        self.obj.save()
        self.assertEqual(1, self.obj.pk)

    def testHasCreatedAt(self):
        'Subscription must have automatic created_at'
        self.obj.save()
        self.assertIsInstance(self.obj.created_at, datetime)

    def testUnicode(self):
        self.assertEqual(u'Matheus Moreira', unicode(self.obj))

    def test_paid_default_value_is_False(self):
        'By default paid must be False.'
        self.assertEqual(False, self.obj.paid)


class SubscriptionUniqueTest(TestCase):
    def setUp(self):
        # Create a first entry to force collision
        Subscription.objects.create(
            name='Matheus Moreira',
            cpf='01234567890',
            email='matheus@moreira.com.br',
            phone='(21) 98888-7777'
        )

    def testCPFUnique(self):
        'CPF must be unique'
        s = Subscription(
            name='Matheus Moreira',
            cpf='01234567890',
            email='outro@moreira.com.br',
            phone='(21) 98888-7777'
        )
        self.assertRaises(IntegrityError, s.save)

    def testEmailUnique(self):
        'Email must be unique'
        s = Subscription(
            name='Matheus Moreira',
            cpf='99999999999',
            email='matheus@moreira.com.br',
            phone='(21) 98888-7777'
        )
        self.assertRaises(IntegrityError, s.save)
