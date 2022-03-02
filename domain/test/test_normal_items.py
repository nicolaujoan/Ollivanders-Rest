import pytest
from gilded_rose import NormalItem
from test_collector import TestAutomata

# elixir (day 0)
elixir = NormalItem("Elixir of the Mongoose", 5, 7)
ELIXIR_EXPECTED_REPS = TestAutomata.getExpectedReps("stdout.gr", "Elixir")

# dexterity vest (day 0)
dexter = NormalItem("+5 Dexterity Vest", 10, 20)
DEXTER_EXPECTED_REPS = TestAutomata.getExpectedReps("stdout.gr", "+5")


@pytest.mark.elixir
def test_elixir():
    for rep in ELIXIR_EXPECTED_REPS:
        elixir.updateQuality()
        assert elixir.__repr__() == rep


@pytest.mark.dexterity
def test_dexterity():
    for rep in DEXTER_EXPECTED_REPS:
        dexter.updateQuality()
        assert dexter.__repr__() == rep
