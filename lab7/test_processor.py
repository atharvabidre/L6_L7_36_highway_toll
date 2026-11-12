import re

from hypothesis import example, given, strategies as st
import pytest

from processor import parse_plate, trip_cost, axle_class

_PLATE_RE = re.compile(r"^([A-Za-z]{2})-(\d{1,2})-([A-Za-z]{1,3})-(\d{1,4})$")
_TRIP_RE = re.compile(r"^(\d+)\s*[xX]\s*(\d+)$")


@given(st.from_regex(_PLATE_RE, fullmatch=True))
def test_parse_plate_valid_normalizes_state(plate):
    state, district, number = parse_plate(plate)
    assert state == plate[:2].upper()
    assert isinstance(district, int)
    assert isinstance(number, int)


@example("0-0-0-0")
@given(st.text())
def test_parse_plate_rejects_malformed_text(plate):
    if not _PLATE_RE.fullmatch(plate.strip()):
        with pytest.raises((ValueError, TypeError)):
            parse_plate(plate)


@given(st.integers(min_value=0, max_value=10**12), st.integers(min_value=0, max_value=10**12), st.sampled_from(["x", "X"]))
def test_trip_cost_multiplies_nonnegative_parts(count, rate, sep):
    assert trip_cost(f"{count}{sep}{rate}") == count * rate


@example("1x-0")
@given(st.text())
def test_trip_cost_rejects_malformed_text(text):
    if not _TRIP_RE.fullmatch(text.strip()):
        with pytest.raises((ValueError, TypeError)):
            trip_cost(text)


@given(st.integers())
def test_axle_class_positive_count(n):
    if n <= 0:
        with pytest.raises((ValueError, TypeError)):
            axle_class(n)
    elif n == 2:
        assert axle_class(n) == "car"
    elif n <= 4:
        assert axle_class(n) == "truck"
    else:
        assert axle_class(n) == "heavy"


@given(st.text())
def test_axle_class_rejects_non_integer_text(text):
    if not re.fullmatch(r"\+?\d+", text.strip()):
        with pytest.raises((ValueError, TypeError)):
            axle_class(text)
