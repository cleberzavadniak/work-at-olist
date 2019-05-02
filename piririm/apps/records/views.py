from utils.endpoints import CommonDetailEndpoint, CommonListEndpoint

from .models import CallStartRecord, CallEndRecord


class CallStartRecordListEndpoint(CommonListEndpoint):
    model = CallStartRecord


class CallStartRecordDetailEndpoint(CommonDetailEndpoint):
    model = CallStartRecord


class CallEndRecordListEndpoint(CommonListEndpoint):
    model = CallEndRecord


class CallEndRecordDetailEndpoint(CommonDetailEndpoint):
    model = CallEndRecord
