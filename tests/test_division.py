from utils import division
import pytest

@pytest.mark.parametrize("a, b, result", [(10, 2, 5),
                                          (20, 10, 2),
                                          (2, 2, 1),
                                          (5, 2, 2.5),
                                          (-4, 2, -2)])
def test_division(a, b, result):
    assert division(a, b) == result 
