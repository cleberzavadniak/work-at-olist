from django.urls import reverse

import pytest


pytestmark = pytest.mark.django_db


def test_create_charge_entry(client):
    url = reverse('charge-entries-list')
    response = client.post(url, {'price': '99.90'})
    assert response.status_code == 405, str(response.content, 'utf-8')


def test_list_charge_entrys(client, charge_entry):
    url = reverse('charge-entries-list')
    response = client.get(url)
    assert response.status_code == 200, str(response.content, 'utf-8')

    response_data = response.json()
    assert len(response_data['results']) == 1
    assert response_data['count'] == 1
    assert response_data['total'] == 1

    first_result = response_data['results'][0]
    assert 'id' in first_result
    assert first_result['id'] == charge_entry.id


def test_list_empty_charge_entrys(client):
    url = reverse('charge-entries-list')
    response = client.get(url)
    assert response.status_code == 200, str(response.content, 'utf-8')

    response_data = response.json()
    assert len(response_data['results']) == 0
    assert response_data['count'] == 0
    assert response_data['total'] == 0
