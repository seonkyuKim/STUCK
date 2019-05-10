# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Hashtags(models.Model):
    id = models.BigAutoField(primary_key=True)
    username = models.ForeignKey('User', models.DO_NOTHING, db_column='username')
    tag = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'Hashtags'


class User(models.Model):
    username = models.CharField(primary_key=True, max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    bio = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'User'


