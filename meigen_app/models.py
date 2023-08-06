from django.db import models

class User(models.Model):
    name = models.CharField(max_length=128)
    hspw = models.CharField(max_length=128)

class Group(models.Model):
    name = models.CharField(max_length=128) 

class Meigener(models.Model):
    name = models.CharField(max_length=128)
    group_id = models.ForeignKey(Group, on_delete=models.CASCADE)

class UserGroup(models.Model):
    group_id = models.ForeignKey(Group, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

class Meigen(models.Model):
    meigen = models.CharField(max_length=1024)
    meigener = models.ForeignKey(Meigener, on_delete=models.CASCADE)
