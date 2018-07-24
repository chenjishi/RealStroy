from django.conf.urls import url

from . import views

app_name = 'stories'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^tag/(\d+)/$', views.tag, name='tag'),
    url(r'^post/(\d+)/$', views.post, name='post'),
    url(r'^submit/$', views.submit, name='submit'),
    url(r'^create_story/$', views.create_story, name='create_story'),
    url(r'^sign_up/$', views.sign_up, name='sign_up'),
    url(r'^auth/$', views.user_auth, name='auth')
]