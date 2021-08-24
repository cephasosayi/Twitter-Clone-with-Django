from django.db import models
from swivapp.models import Swiv
from django.urls import reverse_lazy
from .signals import persed_hashtags
# Create your models here.
class Hashtag(models.Model):
	tag = models.CharField(max_length=120)
	timestamp = models.DateTimeField(auto_now=True)

	def get_absolute_url(self):
		return reverse_lazy("hashtag", kwargs={"hashtag": self.tag })

	def __str__(self):
		return self.tag
	def get_swiv(self):
		return Swiv.objects.filter(content__icontains="#" + self.tag)

def persed_hashtags_receiver(sender, hashtag_list, *args, **kwargs):
	if len(hashtag_list) > 0:
		for tag_var in hashtag_list:
			new_tag, create = Hashtag.objects.get_or_create(tag=tag_var)
	#print(*args)
	#print(**kwargs)
persed_hashtags.connect(persed_hashtags_receiver)