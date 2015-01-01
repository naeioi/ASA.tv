from django.conf.urls import include, patterns, url
from .views import video_player, video_download

urlpatterns = patterns('',
        url(r'^video_player', video_player.as_view()),
        url(r'^video_download', video_download.as_view()),
)
