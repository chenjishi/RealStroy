from django.conf.urls import url

from . import views

app_name = 'stories'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^tag/(\d+)/$', views.tag, name='tag'),
    url(r'^post/(\d+)/$', views.post, name='post')
]