import pytest

from apps.bills.tests.factories import ChargeEntryFactory

pytestmark = pytest.mark.django_db


@pytest.fixture
def charge_entry():
    entry = ChargeEntryFactory()

    diff = entry.end_record.timestamp - entry.start_record.timestamp
    minutes = diff.seconds // 60
    price = (minutes * 0.09) + 0.36
    entry.price = f'{price:.2f}'

    return entry
