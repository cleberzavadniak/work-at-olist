import pytest

from django.conf import settings


pytestmark = pytest.mark.django_db


def test_call_start_record_str(call_start_record):
    assert str(call_start_record.call_id) in str(call_start_record)

    timestamp = call_start_record.timestamp.strftime(settings.DATE_FORMAT)
    assert timestamp in str(call_start_record)


def test_call_start_record_repr(call_start_record):
    assert 'CallStartRecord' in repr(call_start_record)


def test_call_start_record_charge(call_start_record, call_end_record):
    charge_entry = call_start_record.charge()
    assert charge_entry is not None

    assert call_start_record.chargeentry_set.count() == 1


def test_call_start_record_unpaired_charge(call_start_record):
    charge_entry = call_start_record.charge()
    assert charge_entry is None


def test_call_start_record_charge_already_charged(call_start_record,
                                                  call_end_record):
    charge_entry = call_start_record.charge()
    assert charge_entry is not None
    charge_entry2 = call_start_record.charge()
    assert charge_entry2 is not None
    assert charge_entry2.id == charge_entry.id


def test_call_end_record_str(call_end_record):
    assert str(call_end_record.call_id) in str(call_end_record)

    timestamp = call_end_record.timestamp.strftime(settings.DATE_FORMAT)
    assert timestamp in str(call_end_record)


def test_call_end_record_repr(call_end_record):
    assert 'CallEndRecord' in repr(call_end_record)


def test_call_end_record_charge(call_start_record, call_end_record):
    charge_entry = call_end_record.charge()
    assert charge_entry is not None

    assert call_end_record.chargeentry_set.count() == 1


def test_call_end_record_unpaired_charge(call_end_record):
    charge_entry = call_end_record.charge()
    assert charge_entry is None


def test_call_end_record_charge_already_charged(call_start_record,
                                                call_end_record):
    charge_entry = call_end_record.charge()
    assert charge_entry is not None
    charge_entry2 = call_end_record.charge()
    assert charge_entry2 is not None
    assert charge_entry2.id == charge_entry.id
