from __future__ import unicode_literals

from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles


LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())

#This is attendance table class model
class Attendance_table(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    user_id=models.IntegerField()

    class Meta:
        ordering=('created',)
#this table for analysis
class Analysis_table(models.Model):
    user_id = models.IntegerField(blank=False, null=False)
    attendance_date = models.DateField(auto_now_add=True)
    working_hrs = models.FloatField(blank=False, null=False)
    login_time = models.DateTimeField(auto_now_add=False)
    logout_time = models.DateTimeField(auto_now_add=False)
    state  = models.IntegerField(blank=False, null=False)


    class Meta:
        ordering=('attendance_date',)

#this class for GPS application

class Geodata(models.Model):
    user_id = models.IntegerField( blank=True, null=False)
    device_id = models.IntegerField( blank=True, null=False)
    latitude = models.FloatField( blank=True,null=False)
    longitude = models.FloatField( blank=True,null=False)
    speed = models.FloatField(blank=True,null=False)
    time_stamp = models.DateTimeField(auto_now_add = True)

#class Geodata_analysis(models.Models):

#class for SwijiRestaurant app

class SavjiRestaurant(models.Model):
    username = models.CharField( max_length=200, default='0000000', editable=False,blank=True, null=False)
    contact = models.IntegerField( blank=True, null=False)
    item1 = models.CharField( max_length=200, default='0000000', editable=False,blank=True, null=False)
    item2 = models.CharField( max_length=200, default='0000000', editable=False,blank=True, null=False)
    cost = models.FloatField(blank=True,null=False)
    time_stamp = models.DateTimeField(auto_now_add = True)

#class for blog app
class Blog(models.Model):

    title = models.CharField(max_length=250)
    body = models.TextField()
    publish_date = models.DateTimeField('published date')
    topic = models.CharField(max_length=250)
    topic_content = models.TextField()
    code = models.TextField()
    gPlus = models.IntegerField()

    class Meta:

        ordering=('publish_date',)


    def publish_in(self):
        return str(self.publish_date)
    publish_in.short_description = 'publish_date'

    def __unicode__(self):
        return str(self.title)





