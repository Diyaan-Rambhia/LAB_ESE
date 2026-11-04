import numpy as np

np.random.seed(1)

X = np.array([[-1, 1]])
Y = np.array([[-1, 1]])

W = X.T @ Y

x = X.copy()

for _ in range(5):
    y = np.where(x @ W >= 0, 1, -1)
    x = np.where(y @ W >= 0, 1, -1)

print("Input X: ", X)
print("Input Y: ", Y)
print("Input X: ", x)
print("Input Y: ", y)