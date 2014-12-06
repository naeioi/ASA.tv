from django.conf.urls import patterns, url
from .views import InitView, ChunkView, FinalizeView, DestroyView

__all__ = ['exceptions', 'models', 'views']

urlpatterns = patterns(r'upload/',
	url(r'init/?', InitView.as_view(), name='init'),
	url(r'chunk/(?P<owner>[a-fA-F0-9]{64})/?', ChunkView.as_view(), name='chunk'),
	url(r'store/(?P<owner>[a-fA-F0-9]{64})/?', FinalizeView.as_view(), name='store'),
	url(r'destroy/(?P<owner>[a-fA-F0-9]{64}/?)', DestroyView.as_view(), name='destroy'),
)
