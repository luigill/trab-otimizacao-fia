import numpy as np

# Define the function
def f(x):
    n = len(x)
    result = 0
    for i in range(n):
        for j in range(1, 6):
            result += j * np.cos(((j + 1) * x[i]) + j)
    return result

# Compute the gradient of the function
def gradient_f(x):
    n = len(x)
    grad = np.zeros(n)
    for i in range(n):
        for j in range(1, 6):
            grad[i] -= j * (j + 1) * np.sin(((j + 1) * x[i]) + j)
    return grad

# Gradient Descent
def gradient_descent(initial_guess, learning_rate=0.01, max_iter=1000, tol=1e-6):
    x = np.array(initial_guess)
    for i in range(max_iter):
        grad = gradient_f(x)
        x_new = x - learning_rate * grad

        # Check for convergence
        if np.linalg.norm(x_new - x) < tol:
            break

        x = x_new

    return x, f(x)

# Initial guess for x1, x2, x3, x4
initial_guess = np.array([0.0, 0.0, 0.0, 0.0])

# Run gradient descent
optimal_values, min_value = gradient_descent(initial_guess)

print("Optimal values:", optimal_values)
print("Minimum value of the function:", min_value)
