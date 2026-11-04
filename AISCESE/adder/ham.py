W = np.outer(x,x)
net = x @ W
y = np.where(net > 0, 1, -1)


import numpy as np

# Input patterns
X = np.array([
    [1, 0, 0, 0],
    [1, 1, 0, 0],
    [0, 0, 0, 1],
    [0, 0, 1, 1]
])

# Target patterns
T = np.array([
    [0, 1],
    [0, 1],
    [1, 0],
    [1, 0]
])

# Calculate weight matrix
W = np.dot(X.T, T)

print("Weight Matrix:")
print(W)

# Test all inputs
for x in X:
    net = np.dot(x, W)
    y = np.where(net > 0, 1, 0)

    print("\nInput :", x)
    print("Net :", net)
    print("Output:", y)

net = X @ W
y = np.where(net > 0, 1, 0)

print("Net:", net)
print("Output:", y)


import numpy as np

# Input patterns
E = np.array([
    1, 1, 1, 1, -1, -1,
    1, 1, 1, 1, -1, -1,
    1, 1, 1
])

F = np.array([
    1, 1, 1, 1,
    1, 1, 1, -1, -1,
    1, -1, -1,
    1, -1, -1
])

# Target outputs
TE = np.array([-1, 1])
TF = np.array([1, 1])

# Calculate weight matrix
W = np.outer(E, TE) + np.outer(F, TF)

print("Weight Matrix:")
print(W)

# Test E
net_E = E @ W
out_E = np.where(net_E >= 0, 1, -1)

print("\nFor E:")
print("Net:", net_E)
print("Output:", out_E)

# Test F
net_F = F @ W
out_F = np.where(net_F >= 0, 1, -1)

print("\nFor F:")
print("Net:", net_F)
print("Output:", out_F)

