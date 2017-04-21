# Array Manipulator - Python

Written using python3 with pytest.

## Problem Statement

Given an array of length >= 0, and a positive integer N, return the contents of the array divided into N equally sized arrays.

Where the size of the original array cannot be divided equally by N, the final part should have length equal to the remainder.

Example:
```
Inputs [1, 2, 3, 4, 5] and 3
Output [[1, 2], [3, 4], [5]]
```

## To Run Tests (tested on macOS)
```
pip install -r requirements.txt
pytest manipulator_tests.py
```
