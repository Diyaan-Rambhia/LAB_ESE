import numpy as np

X = np.array([[0,0], [0,1], [1,0], [1,1]])
Y = np.array([[0,0], [0,1], [0,1], [1,0]])

def sig(x):
    return 1 / (1 + np.exp(-x))

np.random.seed(1)
w1 = np.random.randn(2,4)
w2 = np.random.randn(4,2)
b1 = np.zeros((1,4))
b2 = np.zeros((1,2))

for _ in range(10000):
    h = sig(X @ w1 + b1)
    o = sig(h @ w2 + b2)

    d2 = (o-Y) * o * (1-o)
    d1 = (d2 @ w2.T) * h * (1-h)

    w2 -= 0.5 * h.T @ d2
    b2 -= 0.5 * d2.mean(axis=0)
    w1 -= 0.5 * X.T @ d1
    b1 -= 0.5 * d1.mean(axis=0)

print("A B Carry Sum")

for x, o in zip(X, sig(sig(X@w1+b1)@w2+b2)):
    print(*x, "  ", *(o >= 0.5).astype(int))