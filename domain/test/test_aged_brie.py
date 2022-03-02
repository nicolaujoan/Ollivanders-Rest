import pytest
from gilded_rose import AgedBrie
from test_collector import TestAutomata

# day 0
cheese = AgedBrie("Aged Brie", 2, 0)

# getting all Aged brie results from stdout.gr
EXPECTED_REPS = TestAutomata.getExpectedReps("stdout.gr", "Aged Brie")


@pytest.mark.aged_brie
def test_update_quality():
    for rep in EXPECTED_REPS:
        cheese.updateQuality()
        assert cheese.__repr__() == rep
