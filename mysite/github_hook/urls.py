from django.conf.urls import patterns, url

from github_hook import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index')
)

