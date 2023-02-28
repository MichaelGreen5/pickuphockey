from django.db import models
from pickuphockey.models import Skate
from django.core.exceptions import ValidationError
import os
from datetime import timedelta, datetime


def validate_sheet_only(value):
    ext = os.path.splitext(value.name)[1]  
    valid_extensions = ['.xlsx', '.xlsm', '.xltx', '.xltm']  # define the valid extensions
    if not ext.lower() in valid_extensions:
        raise ValidationError('File type not supported. Only .xlsx, .xlsm, .xltx, .xltm files are allowed.')


class UploadSheet(models.Model):
    file = models.FileField(upload_to='OrgDash/uploads/',validators=[validate_sheet_only], default= None, null= True, blank= True)


class AutoRecurringSkate(models.Model):
    event = models.ForeignKey(Skate, on_delete=models.CASCADE)
    STATUS_CHOICES = [
        (7,'Every Week'),
        (14,'Every Two Weeks'),
        ('Every Month','Every Month'),
        ('Custom', 'Custom')
    ]
    frequency = models.CharField(max_length=256, choices=STATUS_CHOICES, default ='Every Week')
    days_until_next = models.IntegerField(default=0)
    send_invites_days_before = models.IntegerField(default=1)
    send_invites_time = models.TimeField(auto_now= False)
    send_rosters_hours_before = models.IntegerField(default=1)


    def get_next_skate(self):
        next_event_date = self.event.date + timedelta(days=self.days_until_next)
        send_invites_date = next_event_date - timedelta(days =self.send_invites_days_before)
        send_invites_at = datetime.combine(send_invites_date, self.send_invites_time)
        send_rosters_at = self.event.date - timedelta(hours=self.send_rosters_hours_before)
        return [next_event_date, send_invites_at, send_rosters_at]
    
    def next_skate_date(self): #TODO try this
        if self.frequency == 'Custom':
            next_event_date = self.event.date + timedelta(days=self.days_until_next)
        elif self.frequency == 'Every Month':
            next_event_date = self.event.date + timedelta(months=1)
        else:
            next_event_date = self.event.date + timedelta(days=self.frequency)
        return next_event_date

    
    def __str__(self):
        return self.event.location + ' recurrs every ' + str(self.days_until_next) + ' days'




# Create your models here.
