from django.urls import reverse

import pytest


pytestmark = pytest.mark.django_db


def test_create_call_start_record(client, call_start_record_payload):
    url = reverse('call-start-records-list')
    response = client.post(url, call_start_record_payload)
    assert response.status_code == 201, str(response.content, 'utf-8')


def test_list_call_start_records(client, call_start_record):
    url = reverse('call-start-records-list')
    response = client.get(url)
    assert response.status_code == 200, str(response.content, 'utf-8')

    response_data = response.json()
    assert len(response_data['results']) == 1
    assert response_data['count'] == 1
    assert response_data['total'] == 1

    first_result = response_data['results'][0]
    assert 'id' in first_result
    assert first_result['id'] == call_start_record.id


def test_list_empty_call_start_records(client):
    url = reverse('call-start-records-list')
    response = client.get(url)
    assert response.status_code == 200, str(response.content, 'utf-8')

    response_data = response.json()
    assert len(response_data['results']) == 0
    assert response_data['count'] == 0
    assert response_data['total'] == 0


def test_create_invalid_call_start_record(client, call_start_record_payload):
    url = reverse('call-start-records-list')
    del call_start_record_payload['source']
    response = client.post(url, call_start_record_payload)
    assert response.status_code == 400, str(response.content, 'utf-8')


def test_create_call_end_record(client, call_end_record_payload):
    url = reverse('call-end-records-list')
    response = client.post(url, call_end_record_payload)
    assert response.status_code == 201, str(response.content, 'utf-8')


def test_list_call_end_records(client, call_end_record):
    url = reverse('call-end-records-list')
    response = client.get(url)
    assert response.status_code == 200, str(response.content, 'utf-8')

    response_data = response.json()
    assert len(response_data['results']) == 1
    assert response_data['count'] == 1
    assert response_data['total'] == 1

    first_result = response_data['results'][0]
    assert 'id' in first_result
    assert first_result['id'] == call_end_record.id


def test_create_invalid_call_end_record(client, call_end_record_payload):
    url = reverse('call-end-records-list')
    del call_end_record_payload['call_id']
    response = client.post(url, call_end_record_payload)
    assert response.status_code == 400, str(response.content, 'utf-8')


def test_list_empty_call_end_records(client):
    url = reverse('call-end-records-list')
    response = client.get(url)
    assert response.status_code == 200, str(response.content, 'utf-8')

    response_data = response.json()
    assert len(response_data['results']) == 0
    assert response_data['count'] == 0
    assert response_data['total'] == 0
