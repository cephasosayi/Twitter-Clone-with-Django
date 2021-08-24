from django.views.generic.base import RedirectView
from django.conf.urls import url
from django.contrib import admin
from .views import ( 
	SwivListAPIView,
	SwivCreateAPIView,
	ResharetAPIView,
	LikeToggleAPIView,
    SwivDetailAPIView,
 
)



urlpatterns = [
    url(r'^$',SwivListAPIView.as_view(), name='list'), #api/swivapp
    url(r'^create/$',SwivCreateAPIView.as_view(), name='create'),
    url(r'^(?P<pk>\d+)/reshare/$',ResharetAPIView.as_view(), name='share'),
    url(r'^(?P<pk>\d+)/like/$',LikeToggleAPIView.as_view(), name='like-toggle'),
    url(r'^(?P<pk>\d+)/like/$',SwivDetailAPIView.as_view(), name='detail'),
    #url(r'^(?P<pk>\d+)/update/$',Update.as_view(), name='update'),
    #url(r'^(?P<pk>\d+)/delete/$',Delete.as_view(), name='delete'),


] 

