# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models



class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    def __str__(self):
        return self.username
    class Meta:
        managed = False
        db_table = 'auth_user'

    def __str__(self):
        return self.username






class UserDatabase(models.Model):
    id = models.BigAutoField(primary_key=True)
    username = models.ForeignKey(AuthUser, models.DO_NOTHING, to_field='username', db_column='username', unique=True)
    followers = models.IntegerField()
    influence_points = models.IntegerField()
    flag = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'user_database'

    def __str__(self):
        return self.username


class Influence(models.Model):
    id = models.BigAutoField(primary_key=True)
    username = models.ForeignKey('AuthUser', models.DO_NOTHING, to_field='username', db_column='username')
    name = models.CharField(max_length=50)
    points = models.IntegerField()


    class Meta:
        managed = False
        db_table = 'Influence'
