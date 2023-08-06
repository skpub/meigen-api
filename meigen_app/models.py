from django.db import models

class User(models.Model):
    name = models.CharField(max_length=128)
    hspw = models.CharField(max_length=128)
    class Meta:
        db_table = 'user'

class UserGroup(models.Model):
    group_id = models.BigIntegerField()
    user_id = models.BigIntegerField()
    class Meta:
        db_table = 'user_group'

class Group(models.Model):
    name = models.CharField(max_length=128) 
    class Meta:
        db_table = 'group'

class Meigen(models.Model):
    meigen = models.CharField(max_length=1024)
    group_id = models.BigIntegerField()
    class Meta:
        db_table = 'meigen'
