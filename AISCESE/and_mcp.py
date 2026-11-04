import numpy as np

X = np.array([[0,0], [0,1], [1,0], [1,1]])
Y = np.array([0,0,0,1])

def mcp(x):
    return int(np.sum(x) >= 2)
print("X Y AND")
for x, y in zip(X, Y):
    print(*x, mcp(x))