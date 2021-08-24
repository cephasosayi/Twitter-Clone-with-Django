from django.shortcuts import render
from .models import Hashtag
# Create your views here.
from django.views import View

class HashTagView(View):
	def get(self, request, hashtag, *args,**kwargs):
		obj,created = Hashtag.objects.get_or_create(tag=hashtag)
		return render(request, 'hashtags/tag_view.html', {"obj":obj}
			)