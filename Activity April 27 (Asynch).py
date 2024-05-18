GARBIEL, SHEENALYN M.


import numpy as np
from scipy.optimize import minimize

# Generate synthetic data
np.random.seed(0)
X = np.linspace(0, 10, 50)
true_slope = 2.0
true_intercept = 1.0
y = true_slope * X + true_intercept + np.random.randn(50)

# Define the linear regression model
def linear_regression(params, X, y):
    alpha, beta = params
    y_pred = alpha + beta * X
    error = y_pred - y
    return np.sum(error**2)  # Sum of squared errors as loss function

# Initial guess for parameters (alpha, beta)
initial_guess = [0, 0]

# Use scipy.optimize to find optimal parameters
result = minimize(linear_regression, initial_guess, args=(X, y))

# Extract optimal parameters
alpha_opt, beta_opt = result.x

# Print the estimated parameters
print("Estimated Intercept (alpha):", alpha_opt)
print("Estimated Slope (beta):", beta_op
