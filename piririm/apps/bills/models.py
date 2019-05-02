from django.db import models
from django.conf import settings

from utils.models import SystemBaseModel


class ChargeEntry(SystemBaseModel):
    start_record = models.ForeignKey('records.CallStartRecord', on_delete=models.CASCADE)
    end_record = models.ForeignKey('records.CallEndRecord', on_delete=models.CASCADE)
    price = models.DecimalField(decimal_places=2, max_digits=9)

    @property
    def duration(self):
        diff = self.end_record.timestamp - self.start_record.timestamp
        days = diff.days
        seconds = diff.seconds
        total_seconds = days * 86400 + seconds
        return total_seconds // 60

    @property
    def has_reduced_tariff(self):
        start = self.start_record.timestamp.time()

        for r_start, r_end in settings.REDUCED_TARIFF_PERIODS:
            if start >= r_start and start <= r_end:
                return True

        return False

    @property
    def per_minute_charge(self):
        if self.has_reduced_tariff:
            return settings.REDUCED_PER_MINUTE_CHARGE

        return settings.PER_MINUTE_CHARGE

    @property
    def standing_charge(self):
        return settings.STANDING_CHARGE

    def calculate_price(self):
        return self.duration * self.per_minute_charge + self.standing_charge

    def __str__(self):
        start = self.start_record
        return (
            f'#{start.call_id} '
            f'{start.source}->{start.destination}: '
            f'${self.price} ({self.duration} minutes)'
        )

    def save(self, *args, **kwargs):
        self.price = self.calculate_price()
        return super().save(*args, **kwargs)
