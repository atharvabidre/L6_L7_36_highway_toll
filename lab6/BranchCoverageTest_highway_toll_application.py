
import pytest
from highway_toll import toll_for, toll_charge, pass_advice


# Example test cases (given in the starter file)
def test_ambulance_is_exempt():
    assert toll_charge("ambulance", 2, False, False) == 0


def test_two_axle_base_toll():
    assert toll_for(2, False, False) == 100


# ---- toll_for: axle count validation (True / False of axles < 2) ----
def test_zero_axles_raises():
    with pytest.raises(ValueError):
        toll_for(0, False, False)


def test_one_axle_raises():
    with pytest.raises(ValueError):
        toll_for(1, False, False)


def test_negative_axles_raises():
    with pytest.raises(ValueError):
        toll_for(-3, True, True)


# ---- toll_for: axles in BASE_TOLL (True / False) ----
def test_three_axle_base_toll():
    assert toll_for(3, False, False) == 150


def test_four_axle_base_toll():
    assert toll_for(4, False, False) == 250


def test_five_axle_default_toll():
    assert toll_for(5, False, False) == 400


def test_large_axle_count_default_toll():
    assert toll_for(8, False, False) == 400


# ---- toll_for: is_peak (True / False) ----
def test_peak_two_axle():
    assert toll_for(2, True, False) == 125.0


def test_peak_four_axle():
    assert toll_for(4, True, False) == 312.5


# ---- toll_for: has_fastag (True / False) and axles == 2 (True / False) ----
def test_fastag_two_axle_off_peak():
    assert toll_for(2, False, True) == 90.0


def test_fastag_three_axle_off_peak():
    assert toll_for(3, False, True) == 142.5


def test_fastag_default_axle_off_peak():
    assert toll_for(5, False, True) == 380.0


# ---- toll_for: peak and fastag combined ----
def test_peak_and_fastag_two_axle():
    assert toll_for(2, True, True) == 112.5


def test_peak_and_fastag_five_axle():
    assert toll_for(5, True, True) == 475.0


# ---- toll_charge: exempt (True / False) ----
def test_fire_engine_is_exempt():
    assert toll_charge("fire_engine", 4, True, True) == 0


def test_non_exempt_vehicle_pays_toll():
    assert toll_charge("truck", 3, False, False) == 150


def test_non_exempt_vehicle_invalid_axles_raises():
    with pytest.raises(ValueError):
        toll_charge("car", 1, False, False)


def test_exempt_vehicle_skips_axle_validation():
    assert toll_charge("ambulance", 0, False, False) == 0


# ---- pass_advice: loop and the >, == comparisons ----
def test_pass_advice_buy_pass():
    assert pass_advice([(False, False), (False, False)], 2, 150) == "buy_pass"


def test_pass_advice_either_at_exact_cost():
    assert pass_advice([(False, False), (False, False)], 2, 200) == "either"


def test_pass_advice_pay_per_trip():
    assert pass_advice([(False, False), (False, False)], 2, 300) == "pay_per_trip"


def test_pass_advice_empty_trips_zero_price_is_either():
    assert pass_advice([], 2, 0) == "either"


def test_pass_advice_empty_trips_positive_price_is_pay_per_trip():
    assert pass_advice([], 2, 500) == "pay_per_trip"


def test_pass_advice_mixed_trips_with_peak_and_fastag():
    trips = [(True, True), (False, False), (True, False)]
    # 112.5 + 100 + 125 = 337.5
    assert pass_advice(trips, 2, 300) == "buy_pass"
