import pytest

from apps.records.models import CallStartRecord, CallEndRecord

pytestmark = pytest.mark.django_db


def test_create_call_start_record(call_start_record):
    assert call_start_record.pk is not None


def test_delete_call_start_record(call_start_record):
    call_start_record.delete()
    assert CallStartRecord.objects.count() == 0


def test_call_start_record_str(call_start_record):
    assert str(call_start_record.call_id) in str(call_start_record)

    timestamp = call_start_record.timestamp.strftime('%Y-%m-%d %H:%M:%S')
    assert timestamp in str(call_start_record)


def test_call_start_record_repr(call_start_record):
    assert 'CallStartRecord' in repr(call_start_record)


def test_create_call_end_record(call_end_record):
    assert call_end_record.pk is not None


def test_delete_call_end_record(call_end_record):
    call_end_record.delete()
    assert CallEndRecord.objects.count() == 0


def test_call_end_record_str(call_end_record):
    assert str(call_end_record.call_id) in str(call_end_record)

    timestamp = call_end_record.timestamp.strftime('%Y-%m-%d %H:%M:%S')
    assert timestamp in str(call_end_record)


def test_call_end_record_repr(call_end_record):
    assert 'CallEndRecord' in repr(call_end_record)
