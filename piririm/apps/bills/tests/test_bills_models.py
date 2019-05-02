import pytest

from apps.records.models import ChargeEntry

pytestmark = pytest.mark.django_db


def test_create_charge_entry(charge_entry):
    assert charge_entry.pk is not None


def test_delete_charge_entry(charge_entry):
    charge_entry.delete()
    assert ChargeEntry.objects.count() == 0
