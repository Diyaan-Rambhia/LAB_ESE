import numpy as np

np.random.seed(1)

X = np.random.rand(20,2)
Y = (X[:,0] > 0.5).astype(int)

W = np.array([X[Y==0][0], X[Y==1][0]])
C = np.array([0,1])

lr = 0.1

for _ in range(100):
    for x, y in zip(X, Y):
        i = np.argmin(np.linalg.norm(W-x, axis=1))

        if C[i] == y:
            W[i] += lr * (x-W[i])
        else:
            W[i] -= lr * (x-W[i])

print("Predictions:", end=' ')
for x in X[:5]:
    i = np.argmin(np.linalg.norm(W-x, axis=1))
    print(C[i], end=' ')