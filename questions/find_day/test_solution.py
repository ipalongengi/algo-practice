import pytest
from solution import solution

@pytest.mark.parametrize("day", [
    pytest.param("g$as", marks=pytest.mark.xfail),
    pytest.param("g$as", marks=pytest.mark.xfail),
    pytest.param("Mon", marks=pytest.mark.xfail),
])
def test_invalid_input(day):
    with pytest.raises(KeyError):
        solution(day, 2)

@pytest.mark.parametrize("day,k_days,output", [
    ("Tue", 1, "Wed"),
    ("Tue", 7, "Tue"),
    ("Sat", 64, "Sun"),
    ])
def test_valid_input(day, k_days, output):
    assert solution(day, k_days) == output
