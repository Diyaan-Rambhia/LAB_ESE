
import numpy as np

# Input patterns
X=np.array([
    [1,-1,1],
    [-1,1,-1]
])

# Associated output patterns
Y=np.array([
    [1,-1],
    [-1,1]
])

# Initialize weight matrix
W=np.dot(X.T,Y)

print("Weight Matrix:")
print(W)

def activation(x):
    return np.where(x>=0,1,-1)

# Forward recall: X to Y
for i in range(len(X)):

    x=X[i]
    y=activation(np.dot(x,W))

    # Backward recall: Y to X
    x_new=activation(np.dot(y,W.T))

    print("\nInput X:",x)
    print("Recalled Y:",y)
    print("Recalled X:",x_new)

