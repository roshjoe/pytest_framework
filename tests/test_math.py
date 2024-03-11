import pytest


def add_two_numbers(a, b):
    return a + b


@pytest.mark.math
def test_small_numbers():
    assert add_two_numbers(7, 5) == 12, "The sum of 7 and 5 should be 12"


@pytest.mark.math
def test_large_numbers():
    assert add_two_numbers(200, 600) == 800, "The sum of 200 and 600 should be 800"
