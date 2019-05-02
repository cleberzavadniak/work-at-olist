import pytest

from apps.records.tests.factories import (CallStartRecordFactory,
                                          CallEndRecordFactory)


@pytest.fixture
def call_start_record():
    return CallStartRecordFactory()


@pytest.fixture
def call_start_record_payload():
    return {
        'call_id': 33,
        'timestamp': '2016-02-29 12:00:00',
        'source': '11987654321',
        'destination': '4312345678'
    }


@pytest.fixture
def call_end_record():
    return CallEndRecordFactory()


@pytest.fixture
def call_end_record_payload():
    return {
        'call_id': 33,
        'timestamp': '2016-02-29 12:00:00',
    }
