import datetime
from decimal import Decimal

from django.conf import settings
from django.urls import reverse

import pytest


pytestmark = pytest.mark.django_db


def test_get_bill(client, bill):
    url = reverse('bill', kwargs={'source': bill['source']})
    response = client.get(url + '?period=' + bill['period'])
    assert response.status_code == 200, str(response.content, 'utf-8')

    response_data = response.json()
    assert 'price' in response_data
    assert Decimal(response_data['price']) == bill['price']


def test_get_bill_without_period(client, bill):
    now = datetime.datetime.now()

    url = reverse('bill', kwargs={'source': bill['source']})
    response = client.get(url)
    assert response.status_code == 200, str(response.content, 'utf-8')

    response_data = response.json()
    assert 'price' in response_data
    assert Decimal(response_data['price']) == Decimal('0.00')
    assert 'entries' in response_data
    assert len(response_data['entries']) == 0

    assert 'start' in response_data
    assert 'end' in response_data

    start_str = response_data['start']
    start = datetime.datetime.strptime(start_str, settings.DATE_FORMAT)
    end_str = response_data['end']
    end = datetime.datetime.strptime(end_str, settings.DATE_FORMAT)

    first_day = datetime.date(now.year, now.month, 1)
    last_month = first_day - datetime.timedelta(days=1)

    assert start.year == last_month.year
    assert start.month == last_month.month
    assert start.day == 1

    assert end.year == last_month.year
    assert end.month == last_month.month
    assert end.day >= 27
