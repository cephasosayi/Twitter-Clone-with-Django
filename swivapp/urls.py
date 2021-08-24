from django.views.generic.base import RedirectView
from .views import (
SwivDetailView,
SwivListView,
Create,
Update,
Delete,
ReshareView)

from django.conf.urls import url
from django.contrib import admin

app_name = 'swivapp'
app_name = 'account'
app_name = 'profiles'
urlpatterns = [
   # url(r'^admin/', admin.site.urls),
  	url(r'^$',RedirectView.as_view(url="/")),
    url(r'^search/$',SwivListView.as_view(), name='list'),
    url(r'^create/$',Create.as_view(), name='create'),
    url(r'^(?P<pk>\d+)/$',SwivDetailView.as_view(), name='detail'),
    url(r'^(?P<pk>\d+)/reshare/$',ReshareView.as_view(), name='reshare'),
    url(r'^(?P<pk>\d+)/update/$',Update.as_view(), name='update'),
    url(r'^(?P<pk>\d+)/delete/$',Delete.as_view(), name='delete'),


] 
