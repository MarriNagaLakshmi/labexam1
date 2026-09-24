import pytest
from app import sum_list, count_negatives

@pytest.mark.parametrize("numbers, expected", [
    ([], 0),
    ([1, 2, 3], 6),
    ([-1, -2, -3], -6),
    ([1.5, 2.5], 4.0)
])
def test_sum_list(numbers, expected):
    assert sum_list(numbers) == expected

@pytest.mark.parametrize("numbers, expected", [
    ([], 0),
    ([1, 2, 3], 0),
    ([-1, 2, -3], 2)
])
def test_count_negatives(numbers, expected):
    assert count_negatives(numbers) == expected

@pytest.mark.parametrize("numbers, expected", [
    ([], 0),
    ([1, 2, 3], 0),
    ([-1, 2, -3], 2),
    ([1, -1], 1)  # <-- Changed 5 to 1 to fix the test
])
def test_count_negatives(numbers, expected):
    assert count_negatives(numbers) == expected

