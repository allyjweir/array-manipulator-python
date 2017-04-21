import pytest
import manipulator

def test_simple_array():
    assert manipulator.split([1, 2, 3, 4, 5, 6], 3) == [[1, 2], [3, 4], [5, 6]]

def test_complex_array():
    assert manipulator.split([1, 2, 3, 4, 5], 3) == [[1, 2], [3, 4], [5]]

def test_short_array():
    with pytest.raises(ValueError):
        manipulator.split([1,2], 3)

def test_empty_array():
    with pytest.raises(ValueError):
        manipulator.split([], 3)

def test_bad_divisor():
    with pytest.raises(ValueError):
        manipulator.split([1,2,3,4], -8)
