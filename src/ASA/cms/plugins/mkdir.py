from cms.models import *
from .base import baseplugin
from .exceptions import MissArguments, FileExists
from optparse import OptionParser
from copy import deepcopy


class mkdir(baseplugin):

    def __init__(self):
        super(mkdir, self).__init__()
        parser = OptionParser()
        parser.add_option("-p", action="store_true", default=False, dest="p")
        self.parser = parser

    def set_up_a_folder(self, folder, filename):
        subfolder = deepcopy(folder)
        subfolder.id = None
        subfolder.parent_folder = folder
        subfolder.path += filename + "/"
        subfolder.save()

    def process(self, session, args):
        options, args = self.parser.parse_args(args)
        if len(args) == 0:
            raise MissArguments()
        path_str = session['path']
        path_list = args[0].split("/")
        if args[0].startswith("/"):
            path_str = "/"
            path_list.pop(0)
        if args[0].endswith("/"):
            path_list.pop()
        for i in path_list[:-1]:
            next_path_str = path_str + i + '/'
            try:
                Folder.objects.get(path=next_path_str)
            except Exception as e:
                if options.p is True:
                    folder = Folder.objects.get(path=path_str)
                    self.set_up_a_folder(folder, i)
                else:
                    raise e
            path_str = next_path_str
        # "/"
        if len(path_list) == 0:
            raise FileExists("/")
        else:
            next_path_str = path_str + path_list[-1] + '/'
            try:
                Folder.objects.get(path=next_path_str)
            except:
                folder = Folder.objects.get(path=path_str)
                self.set_up_a_folder(folder, path_list[-1])
            else:
                raise FileExists(args[0])
        session['path'] = path_str

process_object = mkdir()
process = process_object.process
