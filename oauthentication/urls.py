from django.conf.urls import patterns, url
from oauthentication import views

urlpatterns = patterns('',
    url(r'^github-connect/$',views.github_connect,{},'github_connect'),
    url(r'^github-callback/$','github_callback',{},'github_callback'),
)