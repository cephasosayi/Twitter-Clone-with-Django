from django.conf.urls import url, include
from django.views.generic.base import RedirectView
from .views import (
    UserDetailView,
    UserFollowView
   )
app_name = 'accounts'

urlpatterns = [   
   url(r'^', include('django.contrib.auth.urls')),
	 #url(r'^(?P<pk>\d+)/$',UserDetailView.as_view(), name='detail'),
   # url(r'^admin/', admin.site.urls),
  	#url(r'^$',RedirectView.as_view(url="/")),
   # url(r'^search/$',SwivListView.as_view(), name='list'),
   # url(r'^create/$',Create.as_view(), name='create'),
	 url(r'^(?P<username>[\w.@+-]+)/$', UserDetailView.as_view(), name='detail'),
	 url(r'^(?P<username>[\w.@+-]+)/follow/$', UserFollowView.as_view(), name='follow'),

   # url(r'^(?P<pk>\d+)/delete/$',Delete.as_view(), name='delete'),


] 
