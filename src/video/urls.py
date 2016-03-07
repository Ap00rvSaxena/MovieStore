from django.conf.urls import include, url
from django.contrib import admin
from .views import (
    video_list,
    video_play,
    video_upload,
    video_update,
    video_delete
    )
urlpatterns = [
    # Examples:
    # url(r'^$', 'moviestr.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    
    # url(r'^list$', 'video.views.video_list', name='list'),
    # url(r'^play/(?P<id>\d+)/$', 'video.views.video_play', name='play'),

    url(r'^list$', video_list, name='list'),
    url(r'^play/(?P<slug>[\w-]+)/$', video_play,name='play'),
    url(r'^update/(?P<slug>[\w-]+)/$', video_update,name='update'),
    url(r'^delete/(?P<slug>[\w-]+)/$', video_delete,name='delete'),
    url(r'^upload$', video_upload, name='upload'),

    ]