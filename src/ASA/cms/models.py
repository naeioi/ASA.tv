from django.db import models


class User(models.Model):
    id = models.AutoField(primary_key=True)
    nick_name = models.CharField(max_length=128)
    register_at = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)
    authority = models.IntegerField()
    # 0 user
    # 1 admin
    # 2 super admin

    def __init__(self, authority=0):
        super(User, self).__init__()
        self.authority = authority


class Group(models.Model):
    id = models.AutoField(primary_key=True)
    members = models.ManyToManyField(User, db_index=True)


class BaseFile(models.Model):
    id = models.AutoField(primary_key=True)
    # access control list
    user_auth_for_read = models.ManyToManyField(
        User,
        related_name="%(class)s_uafr",
        blank=True,
        db_index=True)
    user_auth_for_write = models.ManyToManyField(
        User,
        related_name="%(class)s_uafw",
        blank=True,
        db_index=True)
    user_auth_for_delete = models.ManyToManyField(
        User,
        related_name="%(class)s_uafd",
        blank=True,
        db_index=True)
    group_auth_for_read = models.ManyToManyField(
        Group,
        related_name="%(class)s_gafr",
        blank=True,
        db_index=True)
    group_auth_for_write = models.ManyToManyField(
        Group,
        related_name="%(class)s_gafw",
        blank=True,
        db_index=True)
    group_auth_for_delete = models.ManyToManyField(
        Group,
        related_name="%(class)s_gafd",
        blank=True,
        db_index=True)

    class Meta:
        abstract = True


class Folder(BaseFile):
    super_host = models.ManyToManyField(
        User,
        related_name="super_host",
        blank=True,
        db_index=True)
    host = models.ManyToManyField(
        User,
        related_name="host",
        blank=True,
        db_index=True)
    file = models.ManyToManyField(
        'File',
        related_name="folder",
        blank=True,
        db_index=True)
    parent_folder = models.ForeignKey(
        'self',
        related_name="folder",
        blank=True,
        null=True,
        db_index=True)
    path = models.CharField(max_length=128, unique=True)

    def __str__(self):
        return str(self.path)


class File(BaseFile):
    size = models.BigIntegerField()
    filehash = models.CharField(max_length=64, unique=True)
    filename = models.CharField(max_length=1024)
    created_at = models.DateTimeField()
    finished_at = models.DateTimeField(auto_now_add=True)

'''
if Folder.objects.filter(path='/').count() <= 0:
    new_folder = Folder()
    new_folder.path = '/'
    new_folder.save()
if Folder.objects.filter(path='/home/').count() <= 0:
    new_folder = Folder()
    new_folder.path = '/home/'
    root_folder = Folder.objects.get(path='/')
    new_folder.parent_folder = root_folder
    new_folder.save()
if Folder.objects.filter(path='/public/').count() <= 0:
    new_folder = Folder()
    new_folder.path = '/public/'
    new_folder.save()
'''
