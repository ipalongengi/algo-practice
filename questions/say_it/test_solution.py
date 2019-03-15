import pytest
from solution import say_it


@pytest.mark.parametrize('n, output', [
    (1, 1),
    (6, 312211),
    (10, 13211311123113112211)
])
def test_valid_inputs(n, output):
    assert say_it(n) == output

@pytest.mark.parametrize('n, output', [
    (0, 1),
    (-25, 1),
])
def test_invalid_inputs(n, output):
    assert say_it(n) == output