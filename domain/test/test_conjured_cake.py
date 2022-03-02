import pytest
from gilded_rose import Conjured
from test_collector import TestAutomata

# day 0
mana_cake = Conjured("Conjured Mana Cake", 3, 6)

# getting all Conjured Mana Cake results from stdout.gr
EXPECTED_REPS = TestAutomata.getExpectedReps("stdout.gr", "Conjured")


@pytest.mark.conjured_cake
def test_update_quality():
    for rep in EXPECTED_REPS:
        mana_cake.updateQuality()
        assert mana_cake.__repr__() == rep
