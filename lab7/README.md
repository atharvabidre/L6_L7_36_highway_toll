# Lab 7 - Fuzz Testing

This directory provides the corrected Highway Toll Calculator and Hypothesis fuzz tests.

The handout refers to `processor.py` and `test_processor.py`. The course starter repository uses `highway_toll.py` and `test_highway_toll.py`, so both filename pairs are included. Each test file targets its matching application module.

Install dependencies and run either pair from this directory:

```powershell
python -m pip install hypothesis pytest
python processor.py
python -m pytest -v test_processor.py
```

Or use the starter repository filenames:

```powershell
python highway_toll.py
python -m pytest -v test_highway_toll.py
```
