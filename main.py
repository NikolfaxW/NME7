import numpy as np
import matplotlib.pyplot as plt

def print_hi(name):
    print(f'Hi, {name}')

def approx_equal(num1, num2, tolerance=5*1e-2):
    return abs(num1 - num2) <= tolerance


if __name__ == '__main__':

    x = np.array([-5,-4,-3,-2,-1,0,1,2,3,4,5])
    y = np.array([60.2, 45.3, 30.5, 11.6, 5.2, 3.1, 6.8, 13.2, 32.8, 44.7, 61.5])
    polynom_order = 3

    A = np.zeros((4,4))

    for i in range(polynom_order + 1): #bc polynom of power 3 + 1
        for j in range(polynom_order + 1):
            for k in range(x.shape[0]):
               A[i,j] += pow(x[k], (i+j))
    print("Defeniton of the components for the system of linear equations A*x = b:")
    print("Matrix A:")
    print(A)
    b = np.zeros((4,1))
    for i in range(polynom_order + 1):
        for k in range(x.shape[0]):
            b[i] += y[k]*pow(x[k],i)
    print("Vector b:")
    print(b)
    solution = np.linalg.solve(A, b)
    print("using linalg.solve function in numpy vector x was got:")
    print(solution)
    ##HARD CODED PART
    a = solution[0]
    b = solution[1]
    c = solution[2]
    d = solution[3]
    print("Components of which are used as coefficients for the polynom f(x) = a + b*x + c*x^2 + d*x^3")
    print("a = ", a)
    print("b = ", b)
    print("c = ", c)
    print("d = ", d)
    required_solution = np.array([5.15,0.38,2.35,-0.01])
    are_solutions_equal = True
    for i in range(polynom_order + 1):
        if not approx_equal(required_solution[i],solution[i]):
            are_solutions_equal = False
            break
    if are_solutions_equal:
        print(
            "The results \033[92mARE CLOSE\033[0m to expected result \033[92m a = 5.15, b = 0.38, c = 2.35, d = -0.01\033[0m")
    else:
        print(
            "The results \033[91mARE NOT CLOSE\033[0m to expected result \033[92m a = 5.15, b = 0.38, c = 2.35, d = -0.01\033[0m")

