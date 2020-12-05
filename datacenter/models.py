from django.db import models
from datetime import datetime

class Passcard(models.Model):
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    passcode = models.CharField(max_length=200, unique=True)
    owner_name = models.CharField(max_length=255)

    def __str__(self):
        if self.is_active:
            return self.owner_name
        return f'{self.owner_name} (inactive)'


class Visit(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    passcard = models.ForeignKey(Passcard)
    entered_at = models.DateTimeField()
    leaved_at = models.DateTimeField(null=True)

    def __str__(self):
        return "{user} entered at {entered} {leaved}".format(
            user=self.passcard.owner_name,
            entered=self.entered_at,
            leaved= "leaved at " + str(self.leaved_at) if self.leaved_at else "not leaved"
        )
    
    def get_duration(self):
      date_now = datetime.now()

      if self.leaved_at is None:
        td = date_now - self.entered_at.replace(tzinfo=None)
        return td.total_seconds()

      td =  self.leaved_at.replace(tzinfo=None) - self.entered_at.replace(tzinfo=None)
      return td.total_seconds()
    
    def is_visit_long(self, minutes=60):
      if self.leaved_at is None:
          return False

      duration = self.get_duration() / minutes

      return duration >= minutes
    
    def format_duration(self, duration):
      hours = duration / 3600
      minutes = (duration % 3600) // 60

      return '{}ч {}мин'.format(int(hours), int(minutes))
