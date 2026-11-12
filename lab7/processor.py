import re

_PLATE_RE = re.compile(r"^([A-Za-z]{2})-(\d{1,2})-([A-Za-z]{1,3})-(\d{1,4})$")
_TRIP_RE = re.compile(r"^(\d+)\s*[xX]\s*(\d+)$")


def parse_plate(plate):
    """Parse a plate like KA-05-AB-1234 into state, district, and number."""
    if not isinstance(plate, str):
        raise ValueError("plate must be text")
    match = _PLATE_RE.fullmatch(plate.strip())
    if not match:
        raise ValueError("plate must match SS-DD-SSS-NNNN format")
    state, district, _series, number = match.groups()
    return state.upper(), int(district), int(number)


def trip_cost(text):
    """Calculate trip count times rate from text such as '3x150'."""
    if not isinstance(text, str):
        raise ValueError("trip cost must be text")
    match = _TRIP_RE.fullmatch(text.strip())
    if not match:
        raise ValueError("trip cost must be nonnegative integers in count x rate form")
    count, rate = map(int, match.groups())
    return count * rate


def axle_class(axles):
    """Classify a positive whole axle count as car, truck, or heavy."""
    if isinstance(axles, bool):
        raise ValueError("axle count must be a positive whole number")
    if isinstance(axles, int):
        n = axles
    elif isinstance(axles, str) and re.fullmatch(r"\+?\d+", axles.strip()):
        n = int(axles.strip())
    else:
        raise ValueError("axle count must be a positive whole number")
    if n <= 0:
        raise ValueError("axle count must be positive")
    if n == 2:
        return "car"
    if n <= 4:
        return "truck"
    return "heavy"


def main():
    print("==== Running parse_plate ====")
    try:
        result = parse_plate(input("Enter a plate (e.g. KA-05-AB-1234): "))
        print("State, District and Number:", result)
        print("\n==== Running trip_cost ====")
        result = trip_cost(input("Enter trips x rate (e.g. 3x150): "))
        print("Trip Cost:", result)
        print("\n==== Running axle_class ====")
        result = axle_class(input("Enter an axle count (e.g. 3): "))
        print("Vehicle Class:", result)
    except (ValueError, EOFError) as exc:
        print("Invalid input:", exc)


if __name__ == "__main__":
    main()
