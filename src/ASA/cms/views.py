from django.shortcuts import render
from django.http import HttpResponse
import importlib
from .models import Folder
from .plugins.exceptions import FolderNotFound
import re
plugins = importlib.import_module(__package__+'.plugins')
# import copy
try:
    import simplejson as json
except:
    import json


class NoSuchCommand(Exception):

    def __str__(self):
        return "No such command"


def check_path(path, session):
    return Folder.objects.filter(path=path).count() == 1


def command_line_tool_ajax(request, path, command):
    args = re.split(r' +', command.strip())
    try:
        try:
            plugin = plugins.__dict__[args[0]]
        except Exception as e:
            raise NoSuchCommand()
        args.pop(0)
        path = '/' + path
        if check_path(path, request.session) is False:
            raise FolderNotFound(path)
        request.session['path'] = path
        msg = plugin.process(request.session, args)
    except Exception as e:
        raise e
        return HttpResponse(json.dumps({
            'status': 'error',
            'msg': str(e)}))
    return HttpResponse(json.dumps({'status': 'OK', "msg": msg}))


def command_line_tool(request):
    return render(request, 'command_line_tool.html', {})
