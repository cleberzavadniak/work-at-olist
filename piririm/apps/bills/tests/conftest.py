import datetime

import pytest

from apps.bills.tests.factories import ChargeEntryFactory

from django.conf import settings

pytestmark = pytest.mark.django_db


@pytest.fixture
def charge_entry():
    entry = ChargeEntryFactory()

    diff = entry.end_record.timestamp - entry.start_record.timestamp
    minutes = diff.seconds // 60
    price = (minutes * 0.09) + 0.36
    entry.price = f'{price:.2f}'

    return entry


@pytest.fixture
def not_reduced_charge_entry(charge_entry, not_reduced_period_time):
    reduced_period = settings.REDUCED_TARIFF_PERIODS[0]
    start, end = reduced_period

    start_record = charge_entry.start_record
    new_start = datetime.datetime.combine(start_record.timestamp,
                                          not_reduced_period_time)
    start_record.timestamp = new_start
    start_record.save()

    diff = charge_entry.end_record.timestamp - start_record.timestamp
    minutes = diff.seconds // 60
    price = (minutes * 0.09) + 0.36
    charge_entry.price = f'{price:.2f}'

    return charge_entry
