class baseplugin(object):

    def __init__(self):
        super(baseplugin, self).__init__()


class FolderNotFound(Exception):

    def __init__(self, path):
        self.path = path

    def __str__(self):
        return "no such folder: %s" % self.path


class FileExists(Exception):

    def __init__(self, filename):
        self.filename = filename

    def __str__(self):
        return "%s: File exists" % self.filename


class MissArguments(Exception):

    def __str__(self):
        return "Miss arguments"
