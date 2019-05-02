import pytest

from apps.records.models import CallStartRecord, CallEndRecord

pytestmark = pytest.mark.django_db


def test_create_call_start_record(call_start_record):
    assert call_start_record.pk is not None


def test_delete_call_start_record(call_start_record):
    call_start_record.delete()
    assert CallStartRecord.objects.count() == 0


def test_create_call_end_record(call_end_record):
    assert call_end_record.pk is not None


def test_delete_call_end_record(call_end_record):
    call_end_record.delete()
    assert CallEndRecord.objects.count() == 0
