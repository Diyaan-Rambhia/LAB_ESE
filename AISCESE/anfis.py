import numpy as np

X = np.array([0, 1, 2, 3, 4], dtype=float)
Y = np.array([0, 1, 4, 9, 16], dtype=float)

def gauss(x, c, s):
    return np.exp(-((x-c)**2)/(2*s**2))

# Layer 1: Membership functions
m1 = gauss(X, 0, 2)
m2 = gauss(X, 4, 2)

# Layer 2: Firing strengths
w1 = m1
w2 = m2

# Layer 3: Normalized firing strengths
w1 = w1 / (w1 + w2)
w2 = w2 / (w1 + w2)

# Layer 4: Least squares training
A = np.column_stack([w1*X, w1, w2*X, w2])
P = np.linalg.lstsq(A, Y, rcond=None)[0]

# Layer 5: Final output
O = A @ P

print("Input X: ", X)
print("Input Y: ", Y)
print("Predicted:", np.round(O, 2))