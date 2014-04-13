# coding: utf-8
from django.contrib.auth import get_user_model
from django.test import TestCase
from eventex.myauth.backends import EmailBackend
from django.test.utils import override_settings


class EmailBackendTest(TestCase):
	def setUp(self):
		UserModel = get_user_model()
		UserModel.objects.create_user(
			username='gilbrother',
			email='gilbrother@gmail.com',
			password='123456'
		)
		self.backend = EmailBackend()

	def test_authenticate_with_email(self):
		user = self.backend.authenticate(
			email='gilbrother@gmail.com',
			password='123456'
		)
		self.assertIsNotNone(user)

	def test_wrong_password(self):
		user = self.backend.authenticate(
			email='gilbrother@gmail.com',
			password='eggs!'
		)
		self.assertIsNone(user)

	def test_unknown_user(self):
		user = self.backend.authenticate(
			email='eggs@gmail.com',
			password='eggs!'
		)
		self.assertIsNone(user)

	def test_get_user(self):
		self.assertIsNotNone(self.backend.get_user(1))



class MultipleEmailsTest(TestCase):
	def setUp(self):
		UserModel = get_user_model()
		UserModel.objects.create_user(
			username='user1',
			email='gilbrother@gmail.com',
			password='123456'
		)
		UserModel.objects.create_user(
			username='user2',
			email='gilbrother@gmail.com',
			password='123456'
		)
		self.backend = EmailBackend()

	def test_multiple_emails(self):
		user = self.backend.authenticate(
			email='gilbrother@gmail.com',
			password='123456'
		)
		self.assertIsNone(user)


@override_settings(AUTHENTICATION_BACKENDS=('eventex.myauth.backends.EmailBackend',))
class FunctionalEmailBackendTest(TestCase):
	def setUp(self):
		UserModel = get_user_model()
		UserModel.objects.create_user(
			username='gilbrother',
			email='gilbrother@gmail.com',
			password='123456'
		)

	def test_login_with_email(self):
		result = self.client.login(
			email='gilbrother@gmail.com',
			password='123456'
		)
		self.assertTrue(result)

	def test_login_with_username(self):
		result = self.client.login(
			username='gilbrother@gmail.com',
			password='123456'
		)
		self.assertTrue(result)