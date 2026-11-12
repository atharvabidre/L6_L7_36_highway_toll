@'
# Lab 7 - Fuzz Testing

`processor.py` is the corrected application. It validates input for `parse_plate`, `trip_cost`, and `axle_class`.

`test_processor.py` contains Hypothesis tests for all three functions, including valid inputs, malformed inputs, and boundary values.

The course starter was named `highway_toll.py`; this submission uses the handout's requested filenames.

## Run

Install the dependencies:

```powershell
python -m pip install hypothesis pytest