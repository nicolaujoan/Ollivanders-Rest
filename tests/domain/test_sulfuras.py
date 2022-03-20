import pytest
from domain.gilded_rose import Sulfuras
from test_collector import TestAutomata

# day 0
sulfuras1 = Sulfuras(0, "Sulfuras, Hand of Ragnaros", 0, 80)
sulfuras2 = Sulfuras(1, "Sulfuras, Hand of Ragnaros", -1, 80)

# getting all sulfuras results from stdout.gr
EXPECTED_REPS_1 = []
EXPECTED_REPS_2 = []


@pytest.mark.sulfuras
def test_sulfuras():
    pass