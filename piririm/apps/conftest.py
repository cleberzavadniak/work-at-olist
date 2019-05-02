from datetime import time

import pytest

from django.conf import settings


def pytest_configure():
    settings.STANDING_CHARGE = 100
    settings.PER_MINUTE_CHARGE = 10
    settings.REDUCED_PER_MINUTE_CHARGE = 1

    settings.REDUCED_TARIFF_PERIODS = (
        (time(0, 0, 0), time(11, 59, 59)),
    )


@pytest.fixture
def not_reduced_period_time():
    return time(14, 0, 0)
