# import numpy as np
# import matplotlib.pyplot as plt
import math
import sys

import numpy as np


def print_hi(name):
    print(f'Hi, {name}')


def f(x):
    result = x * x + math.sin(x / 5) - 1 / 4
    return result


def first_derivation_of_f(x):
    result = 2 * x + (1 / 5) * math.cos(x / 5)
    return result


def second_derivation_of_f(x):
    result = 2 - (1 / 25) * math.sin(x / 5)
    return result


if __name__ == '__main__':
    limitations = np.array([0, 100])
    eps = 2 * sys.float_info.epsilon
    print("interval set : [", limitations[0], ";", limitations[1], "]")
    x_0 = (limitations[0] + limitations[1]) / 2
    print("Initial solution set as x_0 = ", x_0)
    iterations = 0
    while (True):
        fx_0 = f(x_0)
        if (fx_0 <= eps):
            break
        dfx_0 = first_derivation_of_f(x_0)
        ddfx_0 = second_derivation_of_f(x_0)
        x_0 = x_0 - (2 * fx_0 * dfx_0) / (2 * fx_0 ** 2 - fx_0 * ddfx_0)
        iterations += 1
    print("By ", iterations, " of Halley's method the a result is :", x_0, " ,which was got with tolerance of ", eps,".")