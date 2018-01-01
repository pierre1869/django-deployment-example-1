from django.conf.urls import url
from templateApp import views
app_name = 'templateApp'

urlpatterns=[
 url(r'^relative/$', views.relative, name='relative'),
 url(r'^other/$', views.other, name='other'),
]
