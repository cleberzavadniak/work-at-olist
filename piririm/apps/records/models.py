import datetime

from django.db import models
from django.conf import settings

from utils.models import SystemBaseModel

from apps.bills.models import ChargeEntry


class BaseCallRecord(SystemBaseModel):
    class Meta:
        abstract = True

    timestamp = models.DateTimeField()
    call_id = models.PositiveIntegerField()


class CallStartRecord(BaseCallRecord, models.Model):
    source = models.CharField(max_length=11)
    destination = models.CharField(max_length=11)

    def __str__(self):
        if isinstance(self.timestamp, datetime.datetime):
            timestamp = self.timestamp.strftime(settings.DATE_FORMAT)
        else:
            timestamp = self.timestamp

        return f'#{self.call_id}, {self.source}->{self.destination}, at {timestamp}'

    def charge(self):
        if not CallEndRecord.objects.filter(call_id=self.call_id).exists():
            return

        end = CallEndRecord.objects.filter(call_id=self.call_id).last()
        return end.charge()


class CallEndRecord(BaseCallRecord, models.Model):
    def __str__(self):
        timestamp = self.timestamp.strftime(settings.DATE_FORMAT)
        return f'#{self.call_id} at {timestamp}'

    def charge(self):
        if not CallStartRecord.objects.filter(call_id=self.call_id).exists():
            return

        start = CallStartRecord.objects.get(call_id=self.call_id)
        charge_entry, _ = ChargeEntry.objects.get_or_create(
            start_record=start,
            end_record=self
        )

        return charge_entry
