import pytest

from django.conf import settings


pytestmark = pytest.mark.django_db


def test_charge_entry_str(charge_entry):
    assert str(charge_entry.start_record.call_id) in str(charge_entry)
    assert str(charge_entry.price) in str(charge_entry)


def test_charge_entry_repr(charge_entry):
    assert 'ChargeEntry' in repr(charge_entry)


def test_charge_entry_duration(charge_entry):
    assert charge_entry.duration == 60


def test_charge_entry_has_reduced_tariff(charge_entry):
    reduced_period = settings.REDUCED_TARIFF_PERIODS[0]
    start, end = reduced_period

    assert charge_entry.start_record.timestamp.time() >= start
    assert charge_entry.start_record.timestamp.time() <= end
    assert charge_entry.has_reduced_tariff is True


def test_charge_entry_has_NOT_reduced_tariff(not_reduced_charge_entry):
    reduced_period = settings.REDUCED_TARIFF_PERIODS[0]
    start, end = reduced_period

    assert not_reduced_charge_entry.start_record.timestamp.time() > end
    assert not_reduced_charge_entry.has_reduced_tariff is False


def test_charge_entry_per_minute_charge(charge_entry):
    assert charge_entry.per_minute_charge == settings.REDUCED_PER_MINUTE_CHARGE
    assert charge_entry.has_reduced_tariff is True


def test_charge_entry_per_minute_charge_not_reduced(not_reduced_charge_entry):
    assert not_reduced_charge_entry.per_minute_charge == settings.PER_MINUTE_CHARGE
    assert not_reduced_charge_entry.has_reduced_tariff is False


def test_charge_entry_standing_charge(charge_entry):
    assert charge_entry.standing_charge == settings.STANDING_CHARGE


def test_charge_entry_calculate_price(charge_entry):
    price = charge_entry.calculate_price()
    expected = 60 * settings.REDUCED_PER_MINUTE_CHARGE + settings.STANDING_CHARGE
    assert price == expected
