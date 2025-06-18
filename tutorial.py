import numpy as np
from scipy.optimize import minimize
# https://www.youtube.com/watch?v=cXHvC_FGx24

def f(x):
    n = len(x)
    result = 0
    for i in range(n):
        for j in range(1, 6):
            result += j * np.cos(((j + 1) * x[i]) + j)
    return result

# Initial guess for x1, x2, x3, x4
initial_guess = np.array([0.0, 0.0, 0.0, 0.0])

# Bounds for each x_i in the range [-10, 10]
bounds = [( -10, 10), ( -10, 10), ( -10, 10), ( -10, 10)]

# Minimize the function
result = minimize(f, initial_guess, bounds=bounds, method = 'SLSQP')

# The optimal values for x1, x2, x3, x4
optimal_values = result.x

print("Optimal values:", optimal_values)
print("Minimum value of the function:", result.fun)