import numpy as np

np.random.seed(1)

X = np.random.choice([-1, 1], size=5)

W = np.outer(X, X)
np.fill_diagonal(W, 0)

Y = np.sign(W@X)

print("Input: ", X)
print("Output: ", Y.astype(int))