import datetime

import factory

from apps.bills.models import ChargeEntry
from apps.records.tests.factories import CallStartRecordFactory, CallEndRecordFactory


class ChargeEntryFactory(factory.DjangoModelFactory):
    class Meta:
        model = ChargeEntry

    start_record = factory.SubFactory(CallStartRecordFactory)
    end_record = factory.SubFactory(CallEndRecordFactory)
    price = '0.00'
