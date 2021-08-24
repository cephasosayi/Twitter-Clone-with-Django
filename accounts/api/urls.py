from django.views.generic.base import RedirectView
from django.conf.urls import url
from django.contrib import admin
from swivapp.api.views import ( 
	SwivListAPIView,
)



urlpatterns = [
    url(r'^(?P<username>[\w.@+-]+)/swivapp/$',SwivListAPIView.as_view(), name='list'), #api/swivapp
   ] 
