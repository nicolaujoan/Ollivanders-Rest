import pytest
from gilded_rose import BackstagePass
from test_collector import TestAutomata

# day 0
backPass1 = BackstagePass("Backstage passes to a TAFKAL80ETC concert", 15, 20)
backPass2 = BackstagePass("Backstage passes to a TAFKAL80ETC concert", 10, 49)
backPass3 = BackstagePass("Backstage passes to a TAFKAL80ETC concert", 5, 49)

# getting all Backstage passes results from stdout.gr
EXPECTED_REPS = TestAutomata.getExpectedReps("stdout.gr", "Backstage passes", 3)
REPS_1 = EXPECTED_REPS[0]
REPS_2 = EXPECTED_REPS[1]
REPS_3 = EXPECTED_REPS[2]


@pytest.mark.back_pass_1
def test_update_quality_1():
    for rep in REPS_1:
        backPass1.updateQuality()
        assert backPass1.__repr__() == rep


@pytest.mark.back_pass_2
def test_update_quality_2():
    for rep in REPS_2:
        backPass2.updateQuality()
        assert backPass2.__repr__() == rep


@pytest.mark.back_pass_1
def test_update_quality_3():
    for rep in REPS_3:
        backPass3.updateQuality()
        assert backPass3.__repr__() == rep
