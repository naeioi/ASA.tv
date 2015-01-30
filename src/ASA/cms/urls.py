from django.conf.urls import url, patterns
from .views import command_line

urlpatterns = patterns(
    '',
    url(
        r"^cms/(?P<path>(([a-z0-9A-Z-_]+/)*))(?P<command>([a-z0-9A-Z-_ /.])+)$",
        command_line,
        name="command_line"
    )
)
