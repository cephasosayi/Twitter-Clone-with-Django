from swivapp.api.serializers import SwivModelSerializer
from ..models import Swiv
from django.db.models import Q
from rest_framework import generics
from rest_framework import permissions
from swivapp.api.pagination import StandardResultsPagination

from rest_framework.views import APIView
from rest_framework.response import Response

from hashtags.models import Hashtag

class TagPostAPIView(generics.ListAPIView):
	queryset = Swiv.objects.all().order_by("-Timestamp")
	serializer_class = SwivModelSerializer
	pagination_class = StandardResultsPagination


	def get_serializer_context(self, *args, **kwargs):
		conntext = super(TagPostAPIView, self).get_serializer_context(*args, **kwargs)
		conntext['request'] = self.request
		return conntext

	def get_queryset(self,*args, **kwargs):
		hashtag = self.kwargs.get("hashtag")
		hashtag_obj = None
		try:
			hashtag_obj = Hashtag.objects.get_or_create(tag=hashtag)
		except:
			pass
		if hashtag_obj:
			qs = hashtag_obj.get_swiv()		
			query = self.request.GET.get("q", None)
			if query is not None:
				qs = qs.filter(
					Q(content__icontains=query) | #complex lookups, check making queries doc
					Q(user__username__icontains=query)
					
					)
			return qs
		return None

