import numpy as np

X = np.array([[0,0], [0,1], [1,0], [1,1]])
Y = np.array([0,0,0,1])

np.random.seed(1)
w = np.random.randn(2)
b = np.random.randn()
lr = 0.1

for _ in range(100):
    for x, y in zip(X, Y):
        o = int(np.dot(x,w) + b >= 0)
        e = y - o
        w += lr * e * x
        b += lr * e

print("Predictions:")
for x in X:
    print(int(np.dot(x,w) + b >= 0))