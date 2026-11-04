import numpy as np

np.random.seed(1)

X = np.random.choice([-1,1], size=(1,3))
Y = np.random.choice([-1,1], size=(1,2))

W = X.T @ Y

O = np.sign(X @ W)

print("Input X:", X)
print("Target Y:", Y)
print("Output Y:", O.astype(int))