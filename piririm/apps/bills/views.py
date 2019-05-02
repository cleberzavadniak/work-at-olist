from utils.endpoints import CommonDetailEndpoint, CommonListEndpoint

from .models import ChargeEntry


class ChargeEntryListEndpoint(CommonListEndpoint):
    model = ChargeEntry
    methods = ['GET']


class ChargeEntryDetailEndpoint(CommonDetailEndpoint):
    model = ChargeEntry
    methods = ['GET']
