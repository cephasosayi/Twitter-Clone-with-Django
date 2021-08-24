from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from .models import Swiv
# Create your tests here.


User=get_user_model()

class SwivModelTest(TestCase):
	def setUp(self):
		some_random_text=User.objects.create(username='google')


	def test_swiv_items(self):
		obj = Swiv.objects.create(
			user=User.objects.first(),
			content="we the best"
			)

		self.assertTrue(obj.content=="we the best")
		self.assertTrue(obj.id==1)
		absolute_url=reverse("swivapp:detail", kwargs={"pk": 1})
		self.assertEqual(obj.get_absolute_url(), absolute_url)

	def test_swiv_url(self):
			obj = Swiv.objects.create(
			user=User.objects.first(),
			content="we the best"
			)
			absolute_url=reverse("swivapp:detail", kwargs={"pk":obj.pk})
			self.assertEqual(obj.get_absolute_url(), absolute_url)
