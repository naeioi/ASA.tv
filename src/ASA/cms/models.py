from django.db import models
from django.core.exceptions import ValidationError


class User(models.Model):
    id = models.AutoField(primary_key=True)
    nick_name = models.CharField(max_length=128)
    passwd = models.CharField(max_length=128)
    register_at = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)
    authority = models.IntegerField(default=0)
    # 0 user
    # 1 admin
    # 2 super admin


class Group(models.Model):
    id = models.AutoField(primary_key=True)
    members = models.ManyToManyField(User, db_index=True)


class BaseFile(models.Model):
    id = models.AutoField(primary_key=True)
    # access control list

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


class ACL(models.Model):
    r = models.BooleanField(default=False)
    w = models.BooleanField(default=False)
    folder = models.ForeignKey('Folder', null=True, blank=True)
    file = models.ForeignKey('File', null=True, blank=True)
    user = models.ForeignKey('User')

    def save(self):
        if (self.file is None) + (self.folder is None) != 1:
            raise Exception("One and only one of file and folder can be set")
        super(ACL, self).__init__()
