import numpy as np

np.random.seed(1)
X = np.random.choice([-1,1], size=5)
W = np.outer(X,X)
np.fill_diagonal(W,0)

# Add noise to input
Y = X.copy()
Y[0] *= -1

# Recall pattern
for _ in range(10):
    for i in range(len(Y)):
        Y[i] = 1 if np.dot(W[i],Y) >= 0 else -1

print("Original:", X)
print("Noisy:", np.where(np.arange(5)==0,-X,Y))
print("Recalled:", Y)