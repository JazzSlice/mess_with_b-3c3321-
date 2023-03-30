from non_linear_stuff import results, iter_info, getFiboNum, getFiboRes, getDixotomicRes, getFooRes, getGoldenRatioRes, printRes
import math
import numpy as np
import matplotlib.pyplot as plt
import pytest

eps1 = 0.001
eps2 = 0.01
eps3 = 0.1
l1 = 0.01
l2 = 0.1

test_layout = [(-1, 4, eps1, l1, '2'),
               (-1, 4, eps1, l2, '2'),
               (-1, 4, eps2, l1, '2'),
               (-1, 4, eps2, l2, '2')]

@pytest.mark.parametrize('a, b, eps, target, foo', test_layout)
def test_opti_methods(a, b, eps, target, foo):
    getDixotomicRes(a, b)
    getGoldenRatioRes(a, b)
    getFiboRes(a, b)

# @pytest.mark.parametrize("a, b, result", [(10, 2, 5),
#                                           (20, 10, 2),
#                                           (2, 2, 1),
#                                           (5, 2, 2.5),
#                                           (-4, 2, -2)])
# def test_division(a, b, result):
#     assert division(a, b) == result 
