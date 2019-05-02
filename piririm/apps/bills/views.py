import datetime
from decimal import Decimal

from django.conf import settings

from powerlibs.django.restless.views import Endpoint

from utils.endpoints import CommonDetailEndpoint, CommonListEndpoint

from .models import ChargeEntry


class ChargeEntryListEndpoint(CommonListEndpoint):
    model = ChargeEntry
    methods = ['GET']


class ChargeEntryDetailEndpoint(CommonDetailEndpoint):
    model = ChargeEntry
    methods = ['GET']


class BillEndpoint(Endpoint):
    methods = ['GET']

    def get_period_limits(self, request):
        period = request.GET.get('period', None)

        if period is None:
            now = datetime.datetime.now()
            first_day = datetime.date(now.year, now.month, 1)
            last_month = first_day - datetime.timedelta(days=1)
            year = last_month.year
            month = last_month.month
        else:
            parts = period.split('/')
            month = int(parts[0])
            year = int(parts[1])

        start = datetime.date(year, month, 1)
        next_month = start + datetime.timedelta(days=33)
        next_month_first_day = datetime.datetime(next_month.year, next_month.month, 1, 0, 0, 0)
        end = next_month_first_day - datetime.timedelta(seconds=1)

        return start, end

    def get(self, request, source, *args, **kwargs):
        start, end = self.get_period_limits(request)

        entries = []
        total_price = Decimal('0.00')

        for entry in ChargeEntry.objects.filter(
            start_record__source=source,
            end_record__timestamp__gte=start,
            end_record__timestamp__lte=end
        ).order_by('start_record__timestamp'):
            start = entry.start_record.timestamp
            end = entry.end_record.timestamp

            entries.append({
                'destination': entry.start_record.destination,
                'start_date': start.strftime('%Y-%m-%d'),
                'start_time': start.strftime('%H:%M:%S'),
                'duration': entry.duration,
                'price': f'R$ {entry.price}'
            })

            total_price += entry.price

        return {
            'start': start.strftime(settings.DATE_FORMAT),
            'end': end.strftime(settings.DATE_FORMAT),
            'price': str(total_price),
            'entries': entries
        }
