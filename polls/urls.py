from django.conf.urls import patterns, url
from polls import views

urlpatterns = patterns(
    '',
    # # ex: /polls
    # url(r'^$', views.IndexView.as_view(), name='index'),
    # # ex: /polls/
    # url(r'^specifics/(?P<question_id>\d+)/$', views.DetailView.as_view(), name='detail'),
    # # ex: /spolls/5/results
    # url(r'^(?P<question_id>\d+)/results/$', views.ResultsView.as_view(), name='results'),
    # ex: /polls/5/vote


        # ex: /polls
    url(r'^$', views.IndexView.as_view(), name='index'),
    # ex: /polls/
    url(r'^specifics/(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),
    # ex: /spolls/5/results
    url(r'^(?P<pk>\d+)/results/$', views.ResultsView.as_view(), name='results'),
    url(r'^(?P<question_id>\d+)/vote/$', views.vote, name='vote'),
)
