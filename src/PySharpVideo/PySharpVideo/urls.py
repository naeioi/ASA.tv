from django.conf.urls import patterns, include, url
from django.contrib import admin

import video_cms
import chatserver

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'PySharpVideo.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'', include(video_cms)),
    url(r'', include(chatserver)),
)

