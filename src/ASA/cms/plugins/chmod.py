from optparse import OptionParser
import os
from cms.models import Folder
from .base import baseplugin
from .exceptions import MissArguments, WrongArgument


class chmod(baseplugin):

    def __init__(self):
        super(chmod, self).__init__()
        parser = OptionParser()
        self.parser = parser

    def process(self, session, args):
        options, args = self.parser.parse_args(args)
        if len(args) < 2:
            raise MissArguments()
        try:
            mod = int(args[0], 8)
            args.pop(0)
        except Exception:
            raise WrongArgument(0)
        if (0o0 <= mod <= 0o777) is False:
            raise WrongArgument(0)
        not_success = []
        for i in args:
            path = os.path.join(session['path'], i)
            if path.endswith("/"):
                path = path[0:-1]
            try:
                folder = Folder.objects.get(path=path+'/')
            except Exception:
                try:
                    file = Folder.objects.get(path=path)
                except Exception:
                    not_success.append(path)
                else:
                    file.mod = mod
                    file.save()
            else:
                folder.mod = mod
                folder.save()

        if len(not_success) > 0:
            not_success.insert(0, "File not found:")
            return [not_success]
        else:
            return None


process_object = chmod()
process = process_object.process
