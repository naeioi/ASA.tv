import os
import logging

logger = logging.getLogger(__name__)

from django.http import HttpResponseBadRequest, HttpResponseForbidden, HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from django.views.generic import View
from wsgiref.util import FileWrapper
from io import StringIO


class video_player(View):
    @staticmethod
    def get(request, *args, **kwargs):
        return render(request, "video_player.html", {'media': 'hehe'})


const_size = 100000
file_dir = 'video_store'
file_name = '1.mp4'
file_full_dir = os.path.join(file_dir, file_name)

class video_download(View):
    @staticmethod
    def get(request, *args, **kwargs):
        try:
            with open( file_full_dir, "rb") as f:
                HTTP_RANGE = request.META['HTTP_RANGE'].split('-')
                op = int(HTTP_RANGE[0][6:])
                size = os.path.getsize(file_full_dir)
                logger.info('hehe')
                if HTTP_RANGE[1]=='':
                    ed = min(size-1, op+const_size-1)
                else:
                    ed = min(int(HTTP_RANGE[1]), op+const_size-1)
                s = f.read()[op:ed+1]
                response = HttpResponse(s, content_type='video/mp4')
                response.status_code = 206
                response['Accept-Ranges'] = 'bytes'
                response['Content-Length'] = ed-op+1
                response['Content-Range'] = 'bytes %s-%s/%s' % (op, ed, size)
                return response
        except Exception as e:
            logger.info(Exception, e)


# Create your views here.
