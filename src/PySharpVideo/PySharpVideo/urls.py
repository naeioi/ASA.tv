from django.conf.urls import patterns, include, url
from django.contrib import admin

import online_player
import upload

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'PySharpVideo.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^online_player/', include(online_player)),
    url(r'^upload/', include(upload)),
)

