import numpy as np
import matplotlib.pyplot as plt

# Dataset
X = np.array([
    [2, 3],
    [3, 3],
    [3, 4],
    [8, 7],
    [8, 8],
    [9, 8]
])

# Number of clusters
k = 2

# Initial centroids
centroids = np.array([
    [2, 3],
    [8, 7]
])

# Repeat clustering
for i in range(10):

    # Calculate distances
    dist = np.sqrt(np.sum((X[:, np.newaxis] - centroids)**2, axis=2))

    # Assign clusters
    labels = np.argmin(dist, axis=1)

    # Update centroids
    new_centroids = np.array([
        X[labels == j].mean(axis=0) for j in range(k)
    ])

    if np.all(centroids == new_centroids):
        break

    centroids = new_centroids

print("Final centroids:")
print(centroids)

print("Cluster labels:")
print(labels)

# Plot
plt.scatter(X[:, 0], X[:, 1], c=labels, label="Data Points")
plt.scatter(centroids[:, 0], centroids[:, 1],
            color="red", marker="X", s=200, label="Centroids")

plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.show()
