from rest_framework import serializers
from django.utils.timesince import timesince

from accounts.api.serializers import UserDisplaySerialzer
from swivapp.models import Swiv

class ParentSwivModelSerializer(serializers.ModelSerializer):
	user = UserDisplaySerialzer(read_only=True)
	date_display = serializers.SerializerMethodField()
	timesince = serializers.SerializerMethodField()
	likes = serializers.SerializerMethodField()
	did_like = serializers.SerializerMethodField()


	class Meta:
		model = Swiv
		fields=[
			'id',
			'user',
			'content',
			'Timestamp',
			'date_display',
			'timesince',
			'likes',
			 'did_like',
			]
	def get_did_like(self, obj):
		request = self.context.get("request")
		try:
			user = request.user
			if user.is_authenticated():
				if user in obj.liked.all():
					return True
		except:
			pass
		return False

	def get_likes(self, obj):
		return obj.liked.all().count()
	def get_date_display(self, obj):
		return obj.Timestamp.strftime("%b %d, %Y at %I:%M %p ")


	
	def get_timesince(self, obj):
		return timesince(obj.Timestamp) + "ago"


class SwivModelSerializer(serializers.ModelSerializer):
	parent_id = serializers.CharField(write_only=True, required=False)
	user = UserDisplaySerialzer(read_only=True)
	date_display = serializers.SerializerMethodField()
	timesince = serializers.SerializerMethodField()
	parent= ParentSwivModelSerializer(read_only=True)
	likes = serializers.SerializerMethodField()
	did_like = serializers.SerializerMethodField()

	class Meta:
		model = Swiv
		fields=[
				'id',
				'parent_id',
				'user',
				'content',
				'Timestamp',
				'date_display',
				'timesince',
				'parent',
				'likes',
				'did_like',
				'comment',
				]
		#read_only_field=['comment']

	def get_did_like(self, obj):
		request = self.context.get("request")
		# user = request.user
		try:
			user = request.user
			if user.is_authenticated():
				if user in obj.liked.all():
					return True
		except:
			pass
		return False
	def get_likes(self, obj):
		return obj.liked.all().count()
	def get_date_display(self, obj):
		return obj.Timestamp.strftime("%b %d, %Y at %I:%M %p ")


	
	def get_timesince(self, obj):
		return timesince(obj.Timestamp) + "ago"
