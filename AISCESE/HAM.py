import numpy as np

np.random.seed(1)
X = np.random.choice([-1, 1], size=5)
W = np.outer(X, X)
np.fill_diagonal(W, 0)

# Add noise to input
Y = X.copy()
Y[0] *= -1
noisy = Y.copy()

for _ in range(10):
    for i in range(len(Y)):
        net = np.dot(W[i], Y)
        if net > 0:
            Y[i] = 1
        elif net < 0:
            Y[i] = -1

print("Original:", X)
print("Noisy:", noisy)
print("Recalled:", Y)