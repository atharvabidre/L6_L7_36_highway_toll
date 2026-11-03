
import pytest
from highway_toll import toll_for, toll_charge, pass_advice


# Example test cases (given in the starter file)
def test_ambulance_is_exempt():
    assert toll_charge("ambulance", 2, False, False) == 0


def test_two_axle_base_toll():
    assert toll_for(2, False, False) == 100


# Additional tests: every line of highway_toll.py is executed at least once
def test_invalid_axle_count_raises():
    with pytest.raises(ValueError):
        toll_for(1, False, False)


def test_axle_count_outside_table_uses_default_toll():
    assert toll_for(5, False, False) == 400


def test_peak_hour_surcharge():
    assert toll_for(2, True, False) == 125.0


def test_fastag_discount_two_axle():
    assert toll_for(2, False, True) == 90.0


def test_fastag_discount_multi_axle():
    assert toll_for(3, False, True) == 142.5


def test_toll_charge_normal_vehicle():
    assert toll_charge("truck", 3, False, False) == 150


def test_pass_advice_buy_pass():
    assert pass_advice([(False, False), (False, False)], 2, 150) == "buy_pass"


def test_pass_advice_either():
    assert pass_advice([(False, False), (False, False)], 2, 200) == "either"


def test_pass_advice_pay_per_trip():
    assert pass_advice([(False, False), (False, False)], 2, 300) == "pay_per_trip"
