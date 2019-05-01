import pytest

from apps.records.tests.factories import (CallStartRecordFactory,
                                          CallEndRecordFactory)


@pytest.fixture
def call_start_record():
    return CallStartRecordFactory()


@pytest.fixture
def call_end_record():
    return CallEndRecordFactory()
