from django.db import models

from utils.models import SystemBaseModel

from apps.records.models import CallStartRecord, CallEndRecord


class ChargeEntry(SystemBaseModel):
    start_record = models.ForeignKey(CallStartRecord, on_delete=models.CASCADE)
    end_record = models.ForeignKey(CallEndRecord, on_delete=models.CASCADE)
    price = models.DecimalField(decimal_places=2, max_digits=9)

    @property
    def duration(self):
        diff = self.end_record.timestamp - self.start_record.timestamp
        return diff.seconds // 60

    def __str__(self):
        start = self.start_record
        return (
           f'#{start.call_id} '
           f'{start.source}->{start.destination}: '
           f'${self.price} ({self.duration} minutes)'
        )
