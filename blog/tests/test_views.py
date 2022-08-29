from urllib import response
from django.test import TestCase

class TestPostView(TestCase):

  def testPostList(self):
    response = self.client.get('')
    self.assertEqual(response.status_code, 200)

  def testDraft(self):
    response = self.client.get('/draft')
    self.assertEqual(response.status_code, 200)