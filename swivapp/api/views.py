from .serializers import SwivModelSerializer
from ..models import Swiv
from django.db.models import Q
from rest_framework import generics
from rest_framework import permissions
from .pagination import StandardResultsPagination

from rest_framework.views import APIView
from rest_framework.response import Response

class LikeToggleAPIView(APIView):
    permission_classes =[permissions.IsAuthenticated]
    def get(self, request, pk, format=None):
    	swiv_qs = Swiv.objects.filter(pk=pk)
    	message = "Not allowed"
    	if request.user.is_authenticated():
    		is_liked = Swiv.objects.like_toggle(request.user, swiv_qs.first())       
    		return Response({"liked": is_liked})
	    	return Response({"message": message}, status=400)
    



class ResharetAPIView(APIView):
    permission_classes =[permissions.IsAuthenticated]
    def get(self, request, pk, format=None):
        swiv_qs = Swiv.objects.filter(pk=pk)
        message = "Not allowed"
        if swiv_qs.exists() and swiv_qs.count() == 1:
            #if request.user.is_authenticated():
            new_post = Swiv.objects.reshare(request.user, swiv_qs.first())
            if new_post is not None:
                data = SwivModelSerializer(new_post).data
                return Response(data)
            message = "Cannot reshare the same post in 1 day"
        return Response({"message": message}, status=400)
    

class SwivCreateAPIView(generics.CreateAPIView):
	serializer_class = SwivModelSerializer
	permission_classes =[permissions.IsAuthenticated]


	def perform_create(self, serializers):
		serializers.save(user=self.request.user)



class SwivDetailAPIView(generics.ListAPIView):
	queryset = Swiv.objects.all()
	serializer_class = SwivModelSerializer
	pagination_class = StandardResultsPagination
	permission_classes =[permissions.AllowAny]

	def get_queryset(self, *args, **kwargs):
		post_id= self.kwargs.get("pk")
		qs = Swiv.objects.filter(pk=post_id)
		if qs.exists() and qs.count()==1:
			parent_obj = qs.first()
			qs1 = parent_obj.get_children()
			qs =(qs | qs1).distinct().extra(select={"parent_id_null": 'parent_id IS NULL'})
		return qs.order_by("-parent_id_null", "-Timestamp")


class SearchPostAPIView(generics.ListAPIView):
	queryset = Swiv.objects.all().order_by("-Timestamp")
	serializer_class = SwivModelSerializer
	pagination_class = StandardResultsPagination


	def get_serializer_context(self, *args, **kwargs):
		conntext = super(SearchPostAPIView, self).get_serializer_context(*args, **kwargs)
		conntext['request'] = self.request
		return conntext

	def get_queryset(self,*args, **kwargs):
		qs = self.queryset
		query = self.request.GET.get("q", None)
		if query is not None:
			qs = qs.filter(
				Q(content__icontains=query) | #complex lookups, check making queries doc
				Q(user__username__icontains=query)
				
				)
		return qs




class SwivListAPIView(generics.ListAPIView):
	serializer_class = SwivModelSerializer
	pagination_class = StandardResultsPagination

	def get_serializer_context(self, *args, **kwargs):
		conntext = super(SwivListAPIView, self).get_serializer_context(*args, **kwargs)
		conntext['request'] = self.request
		return conntext

	def get_queryset(self,*args, **kwargs):
		requested_user =self.kwargs.get("username")
		if requested_user:
			qs = Swiv.objects.filter(user__username=requested_user).order_by("-Timestamp")
		else:
			im_following=self.request.user.profiles.get_following()
			qs1= Swiv.objects.filter(user__in=im_following)
			qs2 = Swiv.objects.filter(user=self.request.user)
			qs =(qs1 | qs2).distinct().order_by("-Timestamp")
		query = self.request.GET.get("q", None)
		if query is not None:
			qs = qs.filter(
				Q(content__icontains=query) | #complex lookups, check making queries doc
				Q(user__username__icontains=query)
				
				)
		return qs
