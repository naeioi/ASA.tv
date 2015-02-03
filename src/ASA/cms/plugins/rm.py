from optparse import OptionParser
from cms.models import Folder
from .base import baseplugin
from .exceptions import MissArguments, FolderNotFound
from .cd import process as cd


class rm(baseplugin):

    def __init__(self):
        super(rm, self).__init__()
        parser = OptionParser()
        parser.add_option("-r",
                          action="store_true",
                          default=False,
                          help="recursive call",
                          dest="recursion")
        self.parser = parser

    def process(self, session, args):
        options, args = self.parser.parse_args(args)
        if len(args) == 0:
            raise MissArguments()
        path_list = args[0].split('/')
        if path_list[-1] == "":
            path_list.pop()
        last_file = path_list[-1]
        path_list.pop()
        cd(session, ['/'.join(path_list)])
        path_str = session['path'] + last_file + '/'
        if options.recursion is True:
            result = Folder.objects.filter(path__startswith=path_str)
            if result.exists() is False:
                raise FolderNotFound(path_str)
            result.delete()

process_object = rm()
process = process_object.process
