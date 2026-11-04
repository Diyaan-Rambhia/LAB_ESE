import numpy as np

np.random.seed(1)

X = np.random.rand(10,2)
W = np.random.rand(3,2)

lr = 0.5

for epoch in range(100):
    for x in X:
        d = np.linalg.norm(W-x, axis=1)
        i = np.argmin(d)
        W[i] += lr * (x-W[i])

    lr *= 0.99

print("Winning Neurons:")
for x in X:
    print(np.argmin(np.linalg.norm(W-x, axis=1)), end=' ')