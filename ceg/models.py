from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

from datetime import datetime

# Project class to hold name and date it was created
class Project(models.Model):
    name = models.CharField(max_length=150, default='', unique=True)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.name

# UserProfile is tied to the User class so we can tie
# it with project and phone since User doesn't have those
class UserProfile(models.Model):
    user = models.OneToOneField(User, unique=False)
    phone = models.CharField(max_length=25, default='')
    def __str__(self):
        return str(self.user)

# UserProject connects Project and UserProfile together
# since Django doesn't have a direct way of connecting
# them since UserProfile depends on Project
class UserProject(models.Model):
    user = models.ForeignKey(UserProfile, default='')
    project = models.ForeignKey(Project, default='')
    def __str__(self):
        return str(self.UserProject.user + '' + self.UserProject.project)


# Below is the section that will manage the dataflows page
class Protocol(models.Model):
    name = models.CharField(max_length=50, default='', unique=True)
    def __str__(self):
        return str(self.name)
    class Meta:
        ordering = ['name']

class Baud_Rate(models.Model):
    number = models.CharField(max_length=50, default='', unique=True)
    def __str__(self):
        return str(self.number)
    class Meta:
        ordering = ['number']

# This is the data flow model that holds all the data before the points list
# I was planning on tying it to the points list data by project with ForeignKey
class Data_Flows(models.Model):
    project = models.ForeignKey(Project, default='')
    connection = models.CharField(max_length=50, default='', unique=True)
    version = models.CharField(max_length=50, default='')
    last_update = models.DateTimeField('date published')
    data_from = models.CharField(max_length=50, default='')
    data_to = models.CharField(max_length=50, default='')
    protocol = models.ForeignKey(Protocol, default='')
    baud_rate = models.ForeignKey(Baud_Rate, default='')
    master_name = models.CharField(max_length=100, default='')
    master_port = models.CharField(max_length=20, default='')
    master_address = models.CharField(max_length=10, default='')
    slave_name = models.CharField(max_length=50, default='')
    slave_port = models.CharField(max_length=20, default='')
    slave_address = models.CharField(max_length=10, default='')
    def __str__(self):
        return str(self.project + '' + self.conneciton)
