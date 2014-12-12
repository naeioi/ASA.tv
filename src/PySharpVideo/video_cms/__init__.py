from django.conf.urls import patterns, url, include
from .views import InitView, ChunkView, FinalizeView, DestroyView, MediaView, DownloadView, BarrageView
from django.views.decorators.csrf import csrf_exempt

__all__ = ['exceptions', 'models', 'views']

urlpatterns_upload = patterns('',
        url(r'init/?', csrf_exempt(InitView.as_view()), name='init'),
        url(r'chunk/(?P<owner>[a-fA-F0-9]{64})/?', csrf_exempt(ChunkView.as_view()), name='chunk'),
        url(r'store/(?P<owner>[a-fA-F0-9]{64})/?', csrf_exempt(FinalizeView.as_view()), name='store'),
        url(r'destroy/(?P<owner>[a-fA-F0-9]{64}/?)', csrf_exempt(DestroyView.as_view()), name='destroy'),
)

urlpatterns_download = patterns('',
        url(r'media/(?P<filename>[a-zA-Z0-9_]{1,64})/?', MediaView.as_view()),
        url(r'download/(?P<token>[a-zA-Z0-9]{64})/?', DownloadView.as_view())
)

urlpatterns_barrages = patterns('',
        url(r'barrage/', BarrageView.as_view()),
)


urlpatterns = patterns('',
        url(r'upload/', include(urlpatterns_upload)),
        url(r'', include(urlpatterns_download)),
        url(r'', include(urlpatterns_barrages)),
)
