
import numpy as np
import matplotlib.pyplot as plt

X=np.array([
    [1,1],
    [1,2],
    [2,1],
    [8,8],
    [8,9],
    [9,8]
])

Y=np.array([0,0,0,1,1,1])

# Initial prototype weights
weights=np.array([
    [1,1],
    [8,8]
])

labels=np.array([0,1])

alpha=0.5

for epoch in range(100):

    for i in range(len(X)):

        # Calculate distance
        dist=np.sqrt(np.sum((weights-X[i])**2,axis=1))

        # Find winner
        winner=np.argmin(dist)

        # Update weights
        if labels[winner]==Y[i]:
            weights[winner]+=alpha*(X[i]-weights[winner])
        else:
            weights[winner]-=alpha*(X[i]-weights[winner])

    alpha=alpha*0.99

print("Final weights:")
print(weights)

# Testing
for i in range(len(X)):
    dist=np.sqrt(np.sum((weights-X[i])**2,axis=1))
    winner=np.argmin(dist)
    print(X[i],"Predicted:",labels[winner])

# Plot
plt.scatter(X[:,0],X[:,1],c=Y,label="Input Data")
plt.scatter(weights[:,0],weights[:,1],
            color="red",marker="X",s=150,label="Prototypes")

plt.xlabel("X1")
plt.ylabel("X2")
plt.title("Learning Vector Quantization")
plt.legend()
plt.show()

