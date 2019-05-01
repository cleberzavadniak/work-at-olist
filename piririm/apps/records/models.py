from django.db import models

from utils.models import SystemBaseModel


class BaseCallRecord(SystemBaseModel):
    class Meta:
        abstract = True

    timestamp = models.DateTimeField()
    call_id = models.PositiveIntegerField()


class CallStartRecord(BaseCallRecord, models.Model):
    source = models.CharField(max_length=11)
    destination = models.CharField(max_length=11)

    def __str__(self):
        timestamp = self.timestamp.strftime('%Y-%m-%d %H:%M:%S')
        return f'#{self.call_id}, {self.source}->{self.destination}, at {timestamp}'

    def __repr__(self):
        clsname = self.__class__.__name__
        return f'<{clsname}: {self}>'


class CallEndRecord(BaseCallRecord, models.Model):
    def __str__(self):
        timestamp = self.timestamp.strftime('%Y-%m-%d %H:%M:%S')
        return f'#{self.call_id} at {timestamp}'

    def __repr__(self):
        clsname = self.__class__.__name__
        return f'<{clsname}: {self}>'
