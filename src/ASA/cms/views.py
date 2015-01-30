# from django.shortcuts import render
from django.http import HttpResponse
import importlib
from .models import Folder
from .plugin.base import FolderNotFound
import re
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


def command_line(request, path, command):
    args = re.split(r' +', command.strip())
    try:
        try:
            plugin = importlib.import_module(__package__+'.plugin.'+args[0])
        except ImportError as e:
            raise e
            raise NoSuchCommand()
        args.pop(0)
        path = '/' + path
        if check_path(path, request.session) is False:
            raise FolderNotFound(path)
        request.session['path'] = path
        plugin.process(request.session, args)
    except Exception as e:
        raise e
        return HttpResponse(json.dumps({'msg': str(e)}))
    return HttpResponse(json.dumps({'msg': 'OK'}))
