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

