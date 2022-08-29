from django.test import TestCase

from django.contrib.auth.models import User
from django.db.utils import IntegrityError
from ..models import Post

# Create your tests here.
class Sample(TestCase):
  fixtures = ['user.json']
  def setUp(self):
    # Auth.User
    # self.author = User.objects.create(username="test", password="12345")
    self.author = User.objects.get(id=1)

  def test_countup(self):
    count = Post.objects.all().count()
    self.assertEqual(count, 1)

    # Post.create
    Post.objects.create(author=self.author, title="test", text="new post!!")

    count = Post.objects.all().count()
    self.assertEqual(count, 2)

  def test_invalid_without_title(self):
    with self.assertRaises(IntegrityError):
      # Post.create
      Post.objects.create(author=self.author, title=None, text="new post!!")


