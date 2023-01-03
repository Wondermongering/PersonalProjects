import numpy as np


def lar(X, y, lambda_):
    n, p = X.shape
    beta = np.zeros(p) # initialize coefficients to 0
    active_set = set() # initialize active set to be empty
    inactive_set = set(range(p)) # initialize inactive set to be all variables
    residuals = y.copy() # initialize residuals to be y
    while True:
        # find variable with largest absolute inner product with residuals
        max_inner_product = 0
        max_var = None
        for j in inactive_set:
            inner_product = np.abs(X[:,j].T @ residuals)
            if inner_product > max_inner_product:
                max_inner_product = inner_product
                max_var = j
        # add variable with largest inner product to active set
        if max_var is not None:
            active_set.add(max_var)
            inactive_set.remove(max_var)
        # fit model using only variables in the active set
        beta_active = np.linalg.inv(X[:, [int(x) for x in active_set]].T @ X[:, [int(x) for x in active_set]]) @ X[:, [int(x) for x in active_set]].T @ y
        # check stationarity conditions
        stationarity_violated = False
        for j in active_set:
            if np.abs(X[:,j].T @ residuals) > lambda_:
                stationarity_violated = True
                break
        if not stationarity_violated:
            break
        # if stationarity conditions are violated, update residuals and continue
        residuals = y - X[:, [int(x) for x in active_set]] @ beta_active
    return beta_active, active_set

# define input features
X = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

# define target values
y = np.array([1, 2, 3])

# define regularization parameter
lambda_ = 0.2

beta, active_set = lar(X, y, lambda_)
print(f"Active set: {active_set}")
print(f"Coefficients: {beta}")
