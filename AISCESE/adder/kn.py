import numpy as np

# Dataset
X = np.array([
    [150, 7],
    [170, 8],
    [120, 6],
    [130, 5],
    [160, 7]
])

Y = np.array(["Apple", "Apple", "Orange", "Orange", "Apple"])

# New data
new = np.array([155, 7])
k = 3

# Calculate distances
dist = np.sqrt(np.sum((X-new)**2, axis=1))

# Get nearest neighbours
idx = np.argsort(dist)[:k]

# Get their classes
labels = Y[idx]

# Majority voting
prediction = max(set(labels), key=list(labels).count)

print("Distances:", dist)
print("Nearest neighbours:", labels)
print("Predicted class:", prediction)
