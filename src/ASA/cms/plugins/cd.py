from cms.models import *
from .base import baseplugin
from .exceptions import FolderNotFound


class cd(baseplugin):

    def __init__(self):
        super(cd, self).__init__()

    def process(self, session, args):
        path = session["path"]
        if args[0].startswith("/"):
            path = args[0]
        else:
            path += args[0]
        if not path.endswith("/"):
            path += "/"
        if Folder.objects.filter(path=path).count() == 1:
            session["path"] = path
        else:
            raise FolderNotFound(args[0])

process_object = cd()
process = process_object.process
