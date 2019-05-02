import datetime

import factory

from apps.records.models import CallStartRecord, CallEndRecord


class CallStartRecordFactory(factory.DjangoModelFactory):
    class Meta:
        model = CallStartRecord

    timestamp = datetime.datetime(1970, 1, 1, 2, 34, 56)
    call_id = 1
    source = '11987654321'
    destination = '4312345678'


class CallEndRecordFactory(factory.DjangoModelFactory):
    class Meta:
        model = CallEndRecord

    timestamp = datetime.datetime(1970, 1, 1, 3, 34, 56)
    call_id = 1
