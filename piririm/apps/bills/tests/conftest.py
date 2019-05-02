import datetime
from decimal import Decimal

import pytest

from apps.records.tests.factories import CallStartRecordFactory, CallEndRecordFactory
from apps.bills.tests.factories import ChargeEntryFactory

from django.conf import settings

pytestmark = pytest.mark.django_db


@pytest.fixture
def charge_entry():
    return ChargeEntryFactory()


@pytest.fixture
def not_reduced_charge_entry(charge_entry, not_reduced_period_time):
    reduced_period = settings.REDUCED_TARIFF_PERIODS[0]
    start, end = reduced_period

    start_record = charge_entry.start_record
    new_start = datetime.datetime.combine(start_record.timestamp,
                                          not_reduced_period_time)
    start_record.timestamp = new_start
    start_record.save()

    charge_entry.price = charge_entry.calculate_price()

    return charge_entry


@pytest.fixture
def bill():
    calls = (
        ('1980-01-01 00:00:00', '1980-01-01 00:05:00'),
        ('1980-01-02 00:00:00', '1980-01-02 00:05:00'),
        ('1980-01-03 00:00:00', '1980-01-03 00:05:00'),
    )

    date_format = '%Y-%m-%d %H:%M:%S'
    price = Decimal('0.00')
    source = '4188776655'

    for start_str, end_str in calls:
        start_date = datetime.datetime.strptime(start_str, date_format)
        end_date = datetime.datetime.strptime(end_str, date_format)

        start_record = CallStartRecordFactory(source=source, timestamp=start_date)
        end_record = CallEndRecordFactory(timestamp=end_date)

        charge_entry = ChargeEntryFactory(
            start_record=start_record,
            end_record=end_record
        )
        price += charge_entry.price

    return {'price': price, 'source': source, 'period': '01/1980'}
