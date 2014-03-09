# coding: utf-8
from django.test import TestCase
from django.core.urlresolvers import reverse as r
from eventex.core.models import Speaker


class SpeakerDetailTest(TestCase):
	def setUp(self):
		Speaker.objects.create(
			name='Gil Brother',
			slug='gil-brother',
			url='http://www.youtube.com/user/canalaway',
			description='Humor ácido, variado e sem frescura.')
		url = r('core:speaker_detail', kwargs={'slug': 'gil-brother'})
		self.resp = self.client.get(url)

	def test_get(self):
		'GET should result in 200.'
		self.assertEqual(200, self.resp.status_code)

	def test_template(self):
		'Template should be core/speaker_detail.html'
		self.assertTemplateUsed(self.resp, 'core/speaker_detail.html')

	def test_html(self):
		'Html must contain data.'
		self.assertContains(self.resp, 'Gil Brother')
		self.assertContains(self.resp, 'Humor ácido, variado e sem frescura.')
		self.assertContains(self.resp, 'http://www.youtube.com/user/canalaway')

	def test_context(self):
		'Speaker must be in context.'		
		speaker = self.resp.context['speaker']
		self.assertIsInstance(speaker, Speaker)


class SpeakerDetailTest(TestCase):
	def test_not_found(self):
		'Unknown speaker should result in 404.'
		url = r('core:speaker_detail', kwargs={'slug': 'judith'})
		response = self.client.get(url)
		self.assertEqual(404, response.status_code)
