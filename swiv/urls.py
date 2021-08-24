"""swiv URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from hashtags.views import HashTagView
from django.conf import settings
from django.conf.urls.static import static
from  swivapp.views import SwivListView
from swiv.views import SearchView
from swivapp.api.views import SearchPostAPIView
from hashtags.api.views import TagPostAPIView
from accounts.views import UserregisterView
# from .views import home

app_name = 'accounts'
app_name = 'swivapp'

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',SwivListView.as_view(), name='home'),
    url(r'^search/$',SearchView.as_view(), name='search'),
    url(r'^register/$',UserregisterView.as_view(), name='register'),
    url(r'^api/search/$',SearchPostAPIView.as_view(), name='search-api'),
    url(r'^api/tags/(?P<hashtag>.*)/$',TagPostAPIView.as_view(), name='tag-post-api'),
    url(r'^tags/(?P<hashtag>.*)/$', HashTagView.as_view(), name='hashtag'),
    url(r'^', include('accounts.urls', namespace='profiles')),
    url(r'^swivapp/', include('swivapp.urls', namespace='swivapp')),
    url(r'^api/', include('accounts.api.urls', namespace='profiles-api')),
    url(r'^', include('django.contrib.auth.urls')),
    url(r'^api/swivapp/', include('swivapp.api.urls', namespace='swivapp-api')), #we created a brand new api-url for api module
   
] 

if settings.DEBUG:
	(static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)) 

