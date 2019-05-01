import pytest

from apps.records.models import ChargeEntry

pytestmark = pytest.mark.django_db


def test_create_charge_entry(charge_entry):
    assert charge_entry.pk is not None


def test_delete_charge_entry(charge_entry):
    charge_entry.delete()
    assert ChargeEntry.objects.count() == 0


def test_charge_entry_str(charge_entry):
    assert str(charge_entry.start_record.call_id) in str(charge_entry)
    assert str(charge_entry.price) in str(charge_entry)


def test_charge_entry_repr(charge_entry):
    assert 'ChargeEntry' in repr(charge_entry)
