# coding: utf-8
from django.test import TestCase
from eventex.core.models import Speaker


class SpeakerModelTest(TestCase):
	def setUp(self):
		self.speaker = Speaker(name='Gil Brother',
						       slug='gil-brother',
						       url='http://www.youtube.com/user/canalaway',
						       description='Humor ácido, variado e sem frescura.')
		self.speaker.save()

	def test_create(self):
		'Speaker instance should be saved.'
		self.assertEqual(1, self.speaker.pk)

	def test_unicode(self):
		'Speaker string representation should be the name'
		self.assertEqual(u'Gil Brother', unicode(self.speaker))