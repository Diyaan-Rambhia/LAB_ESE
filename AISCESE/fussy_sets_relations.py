import numpy as np

A = np.array([0.2, 0.5, 0.8])
B = np.array([0.4, 0.7, 0.6])

print("Union:", np.maximum(A, B))
print("Intersection:", np.minimum(A, B))

R = np.array([[0.2, 0.5],
              [0.7, 0.9]])
S = np.array([[0.6, 0.8],
              [0.4, 0.3]])
T = np.zeros((2, 2))

for i in range(2):
    for j in range(2):
        T[i, j] = max(min(R[i, k], S[k, j]) for k in range(2))

print("Composition:\n", T)