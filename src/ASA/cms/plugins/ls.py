from .base import baseplugin
from .cd import process as cd
from cms.models import *


class ls(baseplugin):

    def __init__(self):
        super(ls, self).__init__()

    def process(self, session, args):
        if len(args) > 0:
            cd(session, args)
        path = session['path']
        return list(
            map(
                lambda msg: msg.path,
                Folder.objects.filter(parent_folder__path=path)
            )
        )

process_object = ls()
process = process_object.process
